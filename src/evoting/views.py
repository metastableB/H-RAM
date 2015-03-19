from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives,EmailMessage
from django.contrib.auth.hashers import SHA1PasswordHasher,make_password
from evoting.models import CandidatesList,ListOfNominee,VotersList,Ballot,PostsForElection,ListOfSecretary,SupportersDetails
from sessionapp.models import RoomPreference,UserList,AdminDetail
#By default, Django uses the PBKDF2 algorithm with a SHA256 hash

def evotingHomePage(request):
	return render_to_response('evotingHomePage.html')

def nominationForm(request):
	'''positionsList = []
	temp = []
	allPositions = PostsForElection.objects.all().filter().order_by('hostelsName')
	for i in range(allPositions.count()):
		if (len(temp) == 0):
			temp.append(allPositions[i].hostelsName)
		#tempHostel = allPositions[0].hostel
		if temp[0] == allPositions[i].hostelsName :
			temp.append(allPositions[i].position)
		else:
			positionsList.append(temp)
			temp = []
	positionsList.append(temp)
	return render_to_response('electionNominationForm.html',{'positions':positionsList})'''

	hostelsList = []
	positionsList = []
	temp = []
	hostelCount = 0
	hostel = ''
	allPositions = PostsForElection.objects.all().filter().order_by('hostelsName')
	for i in range(allPositions.count()):
		if(len(temp) == 0):
			hostelsList.append(allPositions[i].hostelsName)
			hostel = allPositions[i].hostelsName
			temp.append(allPositions[i].position)
		elif (hostel == allPositions[i].hostelsName and len(temp)!=0):
			temp.append(allPositions[i].position)
		elif(hostel != allPositions[i].hostelsName):
			hostelsList.append(allPositions[i].hostelsName)
			hostel = allPositions[i].hostelsName
			positionsList.append(temp)
			temp = []
			temp.append(allPositions[i].position)
	positionsList.append(temp)
	return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList})


def adminLogin(request):
	if request.method == 'POST':
		incorrect = "Incorrect Password"
		errors=[]
		valid = False
		validuser = False
		validpassword=False
		username = request.POST['username']
		if (len(username)!=0):
			validuser=True
		else:
			errors.append("Please enter a username.")
			
		password = request.POST['paswrd']
		if (len(password)!=0):
			validpassword=True
		else:
			errors.append("Please enter a password.")
		if(validpassword & validuser):			
			try:
				user = AdminDetail.objects.get(username=username)
			except UserList.DoesNotExist:
				user = None

			if (user):
				if(password == user.password):
					valid=True

				if(valid):
					request.session['adminUsername'] = user.username
					return HttpResponseRedirect('/EVoting/admin/home')
				else:
					errors.append("Password is incorrect.")
					return render_to_response('adminLoginPage.html',{'errors':errors})
			if not user:
				return render_to_response('adminLoginPage.html',{'errors':"Please Enter the correct credentials"})
		else:
			return render_to_response('adminLoginPage.html',{'errors':errors})
	else:
		return render_to_response('adminLoginPage.html')

def adminHomePage(request):
	if 'adminUsername' in request.session:
		return render_to_response('adminHomePage.html')
	else:
		return HttpResponseRedirect('/EVoting/admin')


#this function registers the valid candidates into db
def validateCandidate(request):
	errors = []
	'''errors.append("hello1")
	errors.append("hello2")
	errors.append("hello3")
	errors.append("hello4")
	return render_to_response('electionNominationForm.html',{'errors' : errors})'''

	candidatesRollno = request.POST['candidatesRollno']
	candidatesName = request.POST['candidatesName']
	position = request.POST['position']
	hostel = request.POST['hostel']
	#supporter1 and supporter2 are the rollno of the two supporters
	supporter1 = request.POST['supporter1']
	supporter2 = request.POST['supporter2']
	sent_mail_to_supporter1 = False
	sent_mail_to_supporter2 = False
	if(len(candidatesRollno)!=0 and len(position)!=0 and len(supporter1)!=0 and len(supporter2)!=0):
		#To check if the candidate already exists or not 
		try:
			candidate = CandidatesList.objects.get(candidatesName = candidatesName,candidatesRollNo = candidatesRollno)
		except CandidatesList.DoesNotExist:
			candidate = None
		if not candidate:
			if candidatesRollno == supporter1 or candidatesRollno == supporter2:
				errors.append("You cannot give your roll number as a supporter")
				return render_to_response('successfullNomination.html',{'name' : candidatesRollno})
			else:
				try:
					supporter1Object = UserList.objects.get(rollNumber = supporter1)
				except UserList.DoesNotExist:
					supporter1Object = None

				if not supporter1Object:
					errors.append("Enter a vaid roll number for First Supporter")

				try:
					supporter2Object = UserList.objects.get(rollNumber = supporter2)
				except UserList.DoesNotExist:
					supporter2Object = None

				if not supporter2Object:
					errors.append("Enter a vaid roll number for Second Supporter")

				if supporter2Object and supporter1Object:
					email1 = supporter1Object.emailId;
					email2 = supporter2Object.emailId;
					string1 = candidatesRollno + supporter1
					string2 = candidatesRollno + supporter2
					hashKey1 = make_password(string1)
					hashKey2 = make_password(string2)
					candidatesSupporter = SupportersDetails(candidatesName = candidatesName,candidatesRollNo = candidatesRollno,firstSupporter = supporter1,secondSupporter = supporter2,firstSupporterHashKey = hashKey1,secondSupporterHashKey = hashKey2)
					candidatesSupporter.save()
					if sendmail(email1,supporter1,candidatesName,hashKey1):
						sent_mail_to_supporter1 = True
					else :
						errors.append("Some Error occured!!! Couldn't send email to " + supporter1)

					if sendmail(email2,supporter2,candidatesName,hashKey2):
						sent_mail_to_supporter2 = True
					else :
						errors.append("Some Error occured!!! Couldn't send email to " + supporter2)
					if (sent_mail_to_supporter1 and sent_mail_to_supporter2):
						newCandidate = CandidatesList(candidatesName = candidatesName,candidatesRollNo = candidatesRollno,hostel = hostel,position = position,firstSupporter = supporter1,secondSupporter = supporter2,eligibility = 1)
						newCandidate.save()
						return render_to_response('successfullNomination.html',{'name' : candidatesRollno})
					else:
						return render_to_response('electionNominationForm.html',{'errors' : errors})
				else:
					return render_to_response('electionNominationForm.html',{'errors' : errors})			
		if candidate:
			errors.append("Candidate has already registered")
			return render_to_response('electionNominationForm.html',{'errors' : errors})			
	elif(len(candidatesRollno) == 0):
		errors.append("Please enter the name of the candidate")
		return render_to_response('electionNominationForm.html',{'errors' : errors})
	elif(len(position) == 0):
		errors.append("Please fill the position")
		return render_to_response('electionNominationForm.html',{'errors' : errors})
	elif(len(supporter1) == 0):
		errors.append("Please enter the name of the first supporter")
		return render_to_response('electionNominationForm.html',{'errors' : errors})
	elif(len(supporter2) == 0):
		errors.append("Please enter the name of the second supporter")
		return render_to_response('electionNominationForm.html',{'errors' : errors})


#This fnction creates the final list of candidates who pass all the eligibility criterias
def createFinalNomineesList(request):
	nominees =CandidatesList.objects.all().filter(eligibility = 1)
	ListOfNominee.objects.all().delete()
	for i in range(nominees.count()):
		newCandidate = ListOfNominee(nomineesName = nominees[i].candidatesName,position = nominees[i].position,NumberOfVotes = 0)
		newCandidate.save()
	return HttpResponse("successfully created list of nominee's")


#This function loads the Ballot page where the voter can go and caste his/her vote
def BallotPage(request):
	if 'username' in request.session:
		rollNumber = request.session['member_id']
		username = request.session['username']
		userobject = UserList.objects.get(username=username,rollNumber = rollNumber)
		if userobject :
			try:
				voter = VotersList.objects.get(voterDetails = userobject)
			except VotersList.DoesNotExist:
				voter = None
			if voter:
				hostel = userobject.hostelAlloted

				try:
					positionObject  = PostsForElection.objects.all().filter(hostelsName = hostel)
				except PostsForElection.DoesNotExist:
					positionObject = None
				
				# So the structure is[['postion1','nominee1','nominee2'],['postion2','nominee1','nominee2'],['postion3','nominee1','nominee2']]
				if positionObject:
					differentPositions = []
					for i in range(positionObject.count()):
						nominee = []
						nominee.append(positionObject[i].position)
						#differentPositions.append(positionObject[i])
						nomineeObject = ListOfNominee.objects.all().filter(position = positionObject[i].position,hostel = hostel)
						#return HttpResponse(nomineeObject)
						for j in range(nomineeObject.count()):
							nominee.append(nomineeObject[j].nomineesName)
						differentPositions.append(nominee)

					'''s = "general secretory"
					generalSecretoryNomineesObject = ListOfNominee.objects.all().filter(position = s)
					generalSecretoryNominees = []
					for i in range(generalSecretoryNomineesObject.count()):
						generalSecretoryNominees.append(generalSecretoryNomineesObject[i].nomineesName)
					s = "mess secretory"
					messSecretoryNomineesObject = ListOfNominee.objects.all().filter(position = s)
					messSecretoryNominees = []
					for i in range(messSecretoryNomineesObject.count()):
						messSecretoryNominees.append(messSecretoryNomineesObject[i].nomineesName)
					s = "cultural secretory"
					culturalSecretoryNomineesObject = ListOfNominee.objects.all().filter(position = s)
					culturalSecretoryNominees = []
					for i in range(culturalSecretoryNomineesObject.count()):
						culturalSecretoryNominees.append(culturalSecretoryNomineesObject[i].nomineesName)
					s = "sports secretory"
					sportsSecretoryNomineesObject = ListOfNominee.objects.all().filter(position = s)
					sportsSecretoryNominees = []
					for i in range(sportsSecretoryNomineesObject.count()):
						sportsSecretoryNominees.append(sportsSecretoryNomineesObject[i].nomineesName)'''

					#return render_to_response('Ballotpage.html',{'generalSecretoryNominees' : generalSecretoryNominees,'messSecretoryNominees' : messSecretoryNominees,'culturalSecretoryNominees' : culturalSecretoryNominees,'sportsSecretoryNominees' : sportsSecretoryNominees})
					return render_to_response('Ballotpage.html',{'positionsList':differentPositions})
				if not positionObject:
					return HttpResponse("No positions for elections")
					#TODO print the errors accordingly
			if not voter:
				errors = []
				errors.append("First create Good and Evil Passphrases!!!")
				return render_to_response('createpasswordsforelection.html',{'errors':errors})



	else:
		return HttpResponseRedirect('/login')


#This function returns the html page where the voter can create there good and evil passphrases
def electionPasswordForm(request):
	if 'username' in request.session:
		return render_to_response('createpasswordsforelection.html')
	else:
		return HttpResponseRedirect('/login')

#this function validates the two evil and good passwords
def createElectionPasswords(request):
	if 'username' in request.session:
		rollNumber = request.session['member_id']
		username = request.session['username']
		errors = []
		userobject = UserList.objects.get(username=username,rollNumber = rollNumber)
		if not userobject:
			return HttpResponseRedirect('/login')
		if userobject:
			goodPassword = request.POST['goodpassword']
			evilPassword = request.POST['evilpassword']
			if(goodPassword == evilPassword):
				errors.append("Both good and evil passwordds are same.Please use different passwords")
				return render_to_response('createpasswordsforelection.html',{'errors':errors})
			else:
				try:
					voter = VotersList.objects.get(voterDetails = userobject)
				except VotersList.DoesNotExist:
					voter = None
				#voter = VotersList.objects.get(voterDetails = userobject)
				if not voter:
					user = VotersList(voterDetails = userobject,goodPassword = make_password(goodPassword),evilPassword = make_password(evilPassword))
					user.save()
					return HttpResponse("Successfully created Good and Evil Passphrases!!!")
				if voter:
					return HttpResponse("You already have created both passphrases!!!")
			
	else:
		return HttpResponseRedirect('/login')


#This function records the votes
def recordVote(request):
	if 'username' in request.session:
		rollNumber = request.session['member_id']
		username = request.session['username']
		gs = "general secretory"
		ms = "mess secretory"
		cs = "cultural secretory"
		ss = "sports secretory"
		userobject = UserList.objects.get(username=username,rollNumber = rollNumber)
		passwordUsed = request.POST['password']
		try:
			voter = VotersList.objects.get(voterDetails = userobject)
		except VotersList.DoesNotExist:
			voter = None
		if not voter:
			return HttpResponseRedirect('/electionPasswordForm')
		if voter:
			if(voter.goodPassword == make_password(passwordUsed)):
				try:
					votersBallot = Ballot.objects.get(voter = voter)
				except Ballot.DoesNotExist:
					votersBallot = None
				if not votersBallot:
					if 'generalSecretory' in request.POST :
						generalSecretoryNomineeChoice = request.POST['generalSecretory']
					else:
						generalSecretoryNomineeChoice = " "
					if 'generalSecretory' in request.POST:
						messSecretoryNomineeChoice = request.POST['messSecretory']
					else:
						messSecretoryNomineeChoice = " "
					if 'culturalSecretory' in request.POST:
						culturalSecretoryNomineeChoice = request.POST['culturalSecretory']
					else:
						culturalSecretoryNomineeChoice = " "
					if 'sportsSecretory' in request.POST:
						sportsSecretoryNomineeChoice = request.POST['sportsSecretory']
					else:
						sportsSecretoryNomineeChoice = " "
					position = gs + "," + ms + "," + cs + "," + ss
					vote = generalSecretoryNomineeChoice + "," + messSecretoryNomineeChoice + "," + culturalSecretoryNomineeChoice + "," + sportsSecretoryNomineeChoice
					recoredVoterBallot = Ballot(voter = voter,position = position,nomineeSelected = vote,goodPasswordUsed = 1)
					recoredVoterBallot.save()
					return HttpResponseRedirect('/home')

				if votersBallot:
					if votersBallot.goodPasswordUsed != 1:
						if 'generalSecretory' in request.POST :
							generalSecretoryNomineeChoice = request.POST['generalSecretory']
						else:
							generalSecretoryNomineeChoice = ""
						if 'generalSecretory' in request.POST:
							messSecretoryNomineeChoice = request.POST['messSecretory']
						else:
							messSecretoryNomineeChoice = ""
						if 'culturalSecretory' in request.POST:
							culturalSecretoryNomineeChoice = request.POST['culturalSecretory']
						else:
							culturalSecretoryNomineeChoice = ""
						if 'sportsSecretory' in request.POST:
							sportsSecretoryNomineeChoice = request.POST['sportsSecretory']
						else:
							sportsSecretoryNomineeChoice = ""
						position = gs + "," + ms + "," + cs + "," + ss
						vote = generalSecretoryNomineeChoice + "," + messSecretoryNomineeChoice + "," + culturalSecretoryNomineeChoice + "," + sportsSecretoryNomineeChoice
						recoredVoterBallot = Ballot(voter = voter,position = position,nomineeSelected = vote,goodPasswordUsed = 1)
						recoredVoterBallot.save()
						return HttpResponseRedirect('/home')
					else:
						return HttpResponseRedirect('/home')
			else:
				return HttpResponseRedirect('/home')
				#return HttpResponse(generalSecretoryNomineeChoice+"  "+sportsSecretoryNomineeChoice+"  "+messSecretoryNomineeChoice+"  "+culturalSecretoryNomineeChoice)

	else:
		return HttpResponseRedirect('/login')

def FillElectionPositions(request):
	return render_to_response('positionsForElection.html')

def RecordElectionPositions(request):
	positionsList = request.POST['positionsList']
	hostel = request.POST['hostelName']
	#positions contains the list of all the positions for election.
	errors = []
	positions = []
	i = 0 
	temp = ""
	for char in positionsList:
		if(char != ","):
			temp += char
		elif(char == ","):
			positions.append(temp)
			temp = ""
			i += 1
	positions.append(temp)						#As the last room in the preference was not getting into the array.
	j=0
	for j in range(len(positions)) :
		try:
			checkPosition = PostsForElection.objects.get(hostelsName = hostel,position = positions[j])
		except PostsForElection.DoesNotExist:
			checkPosition = None
		if not checkPosition:
			newposition = PostsForElection(hostelsName = hostel,position = positions[j])
			newposition.save()
		if checkPosition:
			errors.append(positions[j] + " of  " + hostel + " alredy exists")
			return render_to_response('positionsForElection.html',{'errors':errors})
	return render_to_response('successfullyRecordedPosts.html',{'positions':positions,'hostel' : hostel})

#This function is used to send mail to person to_username with the email id to_user_email to confirm  the support for person named for_username

def verifySupport(request,hashedKey):
	#return HttpResponse("your hshkey is " + hashKey)
	try:
		supporter1 = SupportersDetails.objects.get(firstSupporterHashKey = hashedKey)
	except SupportersDetails.DoesNotExist:
		supporter1 = None
	if not supporter1:
		try:
			supporter2 = SupportersDetails.objects.get(secondSupporterHashKey = hashedKey)
		except SupportersDetails.DoesNotExist:
			supporter2 = None
		if supporter2:
			candidatesRollno = supporter2.candidatesRollNo
			candidate = CandidatesList.object.get(candidatesRollNo = candidatesRollno)
			candidate.secondSupportersSupport = 1
			candidate.save()
			return render_to_response('thanksmesssage.html',{'candidatesName':candidate.candidatesName,'supportersName':candidate.secondSupporter,'position':candidate.position,'hostel':candidate.hostel})
	if supporter1:
		candidatesRollno = supporter1.candidatesRollNo
		candidate = CandidatesList.objects.get(candidatesRollNo = candidatesRollno)
		candidate.firstSupportersSupport = 1
		candidate.save()
		return HttpResponse("Thanks for supporting")
		#return render_to_response('thanksmesssage.html',{'candidatesName':candidate.candidatesName,'supportersName':candidate.firstSupporter,'position':candidate.position,'hostel':candidate.hostel})



#TODO:	To send the links by hashing some informationself. 	to_user_email,to_username,for_username,hashedKey
def sendmail(to_user_email,to_username,for_username,hashedKey):
	subject = "Test Mail"
	link = 'http://127.0.0.1:8000/EVoting/verifySupport/' + hashedKey
	message_html = 'Hello ' + to_username + ',  If you support ' + for_username + '  then please click at the link  ' + link + ' If you dont click on the link then it will be considered that your support was declined '
	if send_mail(subject,message_html,'evotingsystemiitp@gmail.com',[to_user_email],fail_silently = False) :
		return True
	else:
		return False
'''def sendmail(request):
	subject = "Test Mail"
	send_mail(subject,"hello",'evotingsystemiitp@gmail.com',['prateekmohanty21@gmail.com'],fail_silently = False)
	return HttpResponse("success")'''

