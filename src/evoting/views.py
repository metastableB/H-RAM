from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives,EmailMessage
from django.contrib.auth.hashers import SHA1PasswordHasher,make_password
from evoting.models import CandidatesList,ListOfNominee,VotersList,Ballot,PostsForElection,ListOfSecretary,SupportersDetails,ListOfHostel
from sessionapp.models import RoomPreference,UserList,AdminDetail
import json
#By default, Django uses the PBKDF2 algorithm with a SHA256 hash

def evotingHomePage(request):
	return render_to_response('evotingHomePage.html')

def charts(request):
	listOfsecretary = []
	#listOfsecretary =  [['X', 'Y', 'Z'], [1, 2, 3], [4, 5, 6]]
	#listOfsecretary.append(['name','votes'])
	listOfsecretary.append(['prateek', 45])
	listOfsecretary.append(['rahul',20])
	listOfsecretary.append(['harshit',10])
	listOfsecretary.append(['don', 30])
	return render_to_response('chartsDemo.html',{'data1':listOfsecretary})

def nominationForm2(request,errors):
	if 'username' in request.session:
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
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
			elif (hostel == allPositions[i].hostelsName and len(temp)!=0):
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
			elif(hostel != allPositions[i].hostelsName):
				hostelsList.append(allPositions[i].hostelsName)
				hostel = allPositions[i].hostelsName
				positionsList.append(temp)
				temp = []
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
		positionsList.append(temp)
		return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors':errors})
	else:
		return HttpResponseRedirect('/login')

def nominationForm1(request):
	if 'username' in request.session:
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
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
			elif (hostel == allPositions[i].hostelsName and len(temp)!=0):
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
			elif(hostel != allPositions[i].hostelsName):
				hostelsList.append(allPositions[i].hostelsName)
				hostel = allPositions[i].hostelsName
				positionsList.append(temp)
				temp = []
				temp.append({'hostel' : hostel,'position' : allPositions[i].position})
		positionsList.append(temp)
		return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'roll':request.session['member_id']})
	else:
		return HttpResponseRedirect('/login')

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
#TODO : use regex to find if the inputs are valid or not
def validateCandidate(request):
	if 'username' in request.session:
		errors = []
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
				user = UserList.objects.get(username = request.session['username'],rollNumber = request.session['member_id'])
			except UserList.DoesNotExist:
				user = None
			if user:
				if user.rollNumber != candidatesRollno:
					errors.append("Please enter your roll number to fill the nomination form.YOU CAN FILL NOMINATION FORM ONLY FOR YOURSELF NOT FOR OTHERS!!!")
					#return render_to_response('electionNominationForm.html',{'errors' : errors})
					return HttpResponseRedirect('/EVoting/nominationForm/' + errors)
				if user.hostelAlloted != hostel:
					errors.append("The hostel doesn't match to the one alloted to you")
					return render_to_response('electionNominationForm.html',{'errors' : errors})
				try:
					candidate = CandidatesList.objects.get(candidatesRollNo = candidatesRollno)
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
			if not user:
				return HttpResponse("some error occured!!!")			
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
	else:
		return HttpResponseRedirect('/login')


#This fnction creates the final list of candidates who pass all the eligibility criterias
def createFinalNomineesList(request):
	if 'adminUsername' in request.session:
		nominees =CandidatesList.objects.all().filter(eligibility = 1)
		ListOfNominee.objects.all().delete()
		for i in range(nominees.count()):
			newCandidate = ListOfNominee(nomineesName = nominees[i].candidatesName,position = nominees[i].position,NumberOfVotes = 0)
			newCandidate.save()
		return HttpResponse("successfully created list of nominee's")
	else:
		return HttpResponseRedirect('/EVoting/admin')


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
						nomineeObject = ListOfNominee.objects.all().filter(position = positionObject[i].position,hostel = hostel)
						for j in range(nomineeObject.count()):
							nominee.append(nomineeObject[j].nomineesName)
						differentPositions.append(nominee)
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
					user = VotersList(voterDetails = userobject,goodPassword = goodPassword,evilPassword = evilPassword)
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
		userObject = UserList.objects.get(username=username,rollNumber = rollNumber)
		usersHostel = userObject.hostelAlloted
		positionList = []
		#list for the order in which we enter the positions and the candidates selected by the voter
		positionObject = PostsForElection.objects.all().filter(hostelsName = usersHostel)
		for i in range(positionObject.count()):
			positionList.append(positionObject[i].position)
		passwordUsed = request.POST['password']
		try:
			voter = VotersList.objects.get(voterDetails = userObject)
		except VotersList.DoesNotExist:
			voter = None
		if not voter:
			return HttpResponseRedirect('/EVoting/electionPasswordForm')
		if voter:
			if(voter.goodPassword == passwordUsed):
				try:
					votersBallot = Ballot.objects.all().filter(voter = voter)
				except Ballot.DoesNotExist:
					votersBallot = None
				# if voter has not used his goodpassword 
				if (votersBallot.count() == 0):
					for i in range(len(positionList)):
						if positionList[i] in request.POST :
							pos = positionList[i]
							vote = request.POST[positionList[i]]
						else:
							pos = positionList[i]
							vote - request.POST[positionList[i]]
						recoredVoterBallot = Ballot(voter = voter,hostel = usersHostel,position = pos,nomineeSelected = vote,goodPasswordUsed = 1)
						recoredVoterBallot.save()
					return HttpResponse('success11')

				else:
					return HttpResponse('success2')
			else:
				return HttpResponse('success4')

	else:
		return HttpResponseRedirect('/login')

#for admin to fill positions for election
def FillElectionPositions(request):
	if 'adminUsername' in request.session:
		listOfHostels  = ListOfHostel.objects.all()
		hostels = []
		for i in range(listOfHostels.count()):
			hostels.append(listOfHostels[i].hostelsName)
		return render_to_response('positionsForElection.html',{'hostels':hostels})
	else:
		return HttpResponseRedirect('/EVoting/admin')

def RecordElectionPositions(request):
	if 'adminUsername' in request.session:
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
			'''if checkPosition:
				errors.append(positions[j] + " of  " + hostel + " alredy exists")
				return render_to_response('positionsForElection.html',{'errors':errors})'''
		return render_to_response('successfullyRecordedPosts.html',{'positions':positions,'hostel' : hostel})
	else:
		return HttpResponseRedirect('/EVoting/admin')

#This function is used to send mail to person to_username with the email id to_user_email to confirm  the support for person named for_username

def verifySupport(request,hashedKey):
	if 'username' in request.session:
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
#take care for people with same names
#this is to be linked with a timer
def finalVoteCount(request):
	#to be completed....
	maxVotes = -1
	allHostels = ListOfHostel.objects.all()
	for hostel in allHostels:
		listOfPositions = PostsForElection.objects.all().filter(hostelsName = hostel.hostelsName)
		for position in listOfPositions:
			listOfNominees = ListOfNominee.objects.all().filter(hostel = hostel.hostelsName,position = position.position)
			for nominee in listOfNominees:
				votes = Ballot.objects.all().filter(hostel = hostel.hostelsName,position = position.position,nomineeSelected = nominee.nomineesName)
				noOfVotes = votes.count()
				nominee.NumberOfVotes = noOfVotes
				nominee.save()
				if noOfVotes > maxVotes:
					name = nominee.nomineesName
					roll = nominee.nomineesRollNo
					maxVotes = noOfVotes
			try:
				sec = ListOfSecretary(hostelsName = hostel.hostelsName,position = position.position,nameOfSecretary = name,rollNoOfSecretary = roll)
			except ListOfSecretary.DoesNotExist:
				sec = None
			if not sec:
				secretary = ListOfSecretary(hostelsName = hostel.hostelsName,position = position.position,nameOfSecretary = name,rollNoOfSecretary = roll)
				secretary.save()
	return HttpResponse('success')

def viewNominees(request):
	if 'username' in request.session:
		listOfNominees = ListOfNominee.objects.all()
		if listOfNominees.count() == 0:
			return HttpResponse("The final list of Nominee's is not yet prepared")
		elif listOfNominees.count() != 0:
			nomineesList = []
			for nominee in listOfNominees:
				nomineesList.append({'hostel':nominee.hostel.upper(),'position':nominee.position.upper(),'name':nominee.nomineesName.upper(),'rollno':nominee.nomineesRollNo})
			return render_to_response('viewNominees.html',{'nomineesList':nomineesList})

	else:
		return HttpResponseRedirect('/login')

def viewFinalResult(request):
	if 'username' in request.session:
		finalList = ListOfSecretary.objects.all()
		if finalList.count() == 0:
			return HttpResponse("The result is not yet decides")
		elif finalList.count() != 0:
			List = []
			for sec in finalList:
				List.append({'hostel' : sec.hostelsName.upper(),'position':sec.position.upper(),'name':sec.nameOfSecretary.upper(),'rollno':sec.rollNoOfSecretary})
			return render_to_response('ListOfSecretaries.html',{'List':List})

	else:
		return HttpResponseRedirect('/login')



