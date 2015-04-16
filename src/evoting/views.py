from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
#from django.http import HttpResponse, HttpResponseRedirect
from django.http import *
from django.template import Context, loader
from django.core.context_processors import csrf
from django.core.mail import send_mail, BadHeaderError,EmailMultiAlternatives,EmailMessage
from django.contrib.auth.hashers import SHA1PasswordHasher,make_password
from evoting.models import CandidatesList,ListOfNominee,VotersList,Ballot,PostsForElection,ListOfSecretary,SupportersDetails,ListOfHostel
from sessionapp.models import RoomPreference,UserList,AdminDetail,AcademicDetails
import json
import random
import datetime
import time

from django.template import Context
from django.template.loader import get_template
#from xhtml2pdf import pisa 
#By default, Django uses the PBKDF2 algorithm with a SHA256 hash

def generate_PDF(request):
	if 'username' in request.session:
	    data = {}

	    template = get_template('viewNominees.html')
	    html  = template.render(Context(data))

	    file = open('test.pdf', "w+b")
	    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
	            encoding='utf-8')

	    file.seek(0)
	    pdf = file.read()
	    file.close()            
	    return HttpResponse(pdf, mimetype='application/pdf')
	else :
		return HttpResponseRedirect('/login')

def evotingHomePage(request):
	if 'username' in request.session:
		return render_to_response('evotingHomePage.html')
	else:
		return HttpResponseRedirect('/login')

def charts(request):
	if 'username' in request.session:
		listOfsecretary = []
		#listOfsecretary =  [['X', 'Y', 'Z'], [1, 2, 3], [4, 5, 6]]
		#listOfsecretary.append(['name','votes'])
		listOfsecretary.append({'name':'prateek1','value':45})
		listOfsecretary.append({'name':'prateek2','value':25})
		listOfsecretary.append({'name':'prateek3','value':35})
		listOfsecretary.append({'name':'prateek','value':15})
		return render_to_response('chartsDemo.html',{'data1':listOfsecretary})
		'''xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
		ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

		extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
		chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
		charttype = "pieChart"

		data = {
		    'charttype': charttype,
		    'chartdata': chartdata,
		}
		return render_to_response('chartsDemo.html', data)'''
	else:
		return HttpResponseRedirect('/login')

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
		if(allPositions.count() != 0):
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
			return render_to_response('messages.html',{'message':"The Election is closed.Please contact the administrator for more details.",'messageTitle':"E-Voting"})
	else:
		return HttpResponseRedirect('/login')

def adminLogout(request):
	if 'adminUsername' in request.session:
		try:
			del request.session['adminUsername']
		except keyError:
			pass
		return HttpResponseRedirect('/administrator')
	else :
		return HttpResponseRedirect('/administrator')

def adminLogin(request):
	if 'adminUsername' in request.session:
		return HttpResponseRedirect('/administrator/home')
	else:
		return render_to_response('adminLoginPage.html')

def adminLoginCheck(request):
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
					return HttpResponseRedirect('/administrator/home')
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
		return HttpResponseRedirect('/administrator')


#this function registers the valid candidates into db
def validateCandidate(request):
	if 'username' in request.session:
		errors = []
		candidatesRollno = request.session['member_id']
		candidatesName = request.POST['candidatesName']
		position = request.POST['position']
		hostel1 = request.POST['hostel']
		#supporter1 and supporter2 are the rollno of the two supporters
		supporter1 = request.POST['supporter1']
		supporter2 = request.POST['supporter2']
		sent_mail_to_supporter1 = False
		sent_mail_to_supporter2 = False
		# List of hostels and positions
		hostelsList = []
		positionsList = []
		temp = []
		hostelCount = 0
		hostel = ''
		allPositions = PostsForElection.objects.all().filter().order_by('hostelsName')
		if(allPositions.count() != 0):
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

		if(len(candidatesRollno)!=0 and len(position)!=0 and len(supporter1)!=0 and len(supporter2)!=0 and len(candidatesName)):
			#To check if the candidate already exists or not
			try:
				user = UserList.objects.get(rollNumber = request.session['member_id'])
			except UserList.DoesNotExist:
				user = None
			if user:
				try:
					userAcademicDetails = AcademicDetails.objects.get(rollNumber = request.session['member_id'])
				except AcademicDetails.DoesNotExist:
					userAcademicDetails = None
				if user.rollNumber != candidatesRollno:
					errors.append("Please enter your roll number to fill the nomination form.YOU CAN FILL NOMINATION FORM ONLY FOR YOURSELF NOT FOR OTHERS!!!")
					return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
				if user.hostelAlloted != hostel1:
					errors.append("The hostel doesn't match to the one alloted to you")
					return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
				try:
					candidate = CandidatesList.objects.get(candidatesRollNo = candidatesRollno)
				except CandidatesList.DoesNotExist:
					candidate = None
				if not candidate:
					if candidatesRollno == supporter1 or candidatesRollno == supporter2:
						errors.append("You cannot give your roll number as a supporter")
						return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
					else:
						try:
							supporter1Object = UserList.objects.get(rollNumber = supporter1)
						except UserList.DoesNotExist:
							supporter1Object = None

						if not supporter1Object:
							errors.append(supporter1+" doesn't exists.Please Enter a valid roll number")

						try:
							supporter2Object = UserList.objects.get(rollNumber = supporter2)
						except UserList.DoesNotExist:
							supporter2Object = None

						if not supporter2Object:
							errors.append(supporter2+" doesn't exists.Please Enter a valid roll number")

						if supporter2Object and supporter1Object:
							try:
								supp1AcademicDetails = AcademicDetails.objects.get(rollNumber = supporter1)
							except AcademicDetails.DoesNotExist:
								supp1AcademicDetails = None
							try:
								supp2AcademicDetails = AcademicDetails.objects.get(rollNumber = supporter2)
							except AcademicDetails.DoesNotExist:
								supp2AcademicDetails = None
							if userAcademicDetails.year == supp1AcademicDetails.year and userAcademicDetails.year == supp2AcademicDetails.year and userAcademicDetails.program == supp1AcademicDetails.program and userAcademicDetails.program == supp2AcademicDetails.program:
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
									return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
							else:
								errors.append("You can only give your supporter from the same year as yours!!!")
								return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
						else:
							return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
				if candidate:
					errors.append("Candidate has already registered")
					return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
			if not user:
				return  render_to_response('messages.html',{'message': username+" ,doesnt exists in db or something is wrong with the sessions",'messageTitle':'E-Voting'})
		elif(len(candidatesName) == 0):
			errors.append("Please enter the name of the candidate")
			return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})			
		elif(len(candidatesRollno) == 0):
			errors.append("Please enter the roll number of the candidate")
			return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
		elif(len(position) == 0):
			errors.append("Please fill the position")
			return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
		elif(len(supporter1) == 0):
			errors.append("Please enter the name of the first supporter")
			return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
		elif(len(supporter2) == 0):
			errors.append("Please enter the name of the second supporter")
			return render_to_response('electionNominationForm.html',{'positions':positionsList,'hostels':hostelsList,'errors' : errors,'roll':request.session['member_id']})
	else:
		return HttpResponseRedirect('/login')


#This fnction creates the final list of candidates who pass all the eligibility criterias
def createFinalNomineesList(request):
	if 'adminUsername' in request.session:
		nominees =CandidatesList.objects.all()
		ListOfNominee.objects.all().delete()
		for i in range(nominees.count()):
			try:
				nomineescpi = AcademicDetails.objects.get(rollNumber = nominees[i].candidatesRollNo)
			except AcademicDetails.DoesNotExist:
				nomineescpi = None
			if nomineescpi:
				if (nominees[i].firstSupportersSupport == 1 and nominees[i].secondSupportersSupport == 1 and nomineescpi.cpi > 6.0):
					newCandidate = ListOfNominee(nomineesName = nominees[i].candidatesName,nomineesRollNo = nominees[i].candidatesRollNo,hostel = nominees[i].hostel,position = nominees[i].position,NumberOfVotes = 0)
					newCandidate.save()
		return render_to_response('adminMessages.html',{'message':"Successfully created list of nominee's",'messageTitle':"E-Voting"})
	else:
		return HttpResponseRedirect('/administrator')


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
					return render_to_response('messages.html',{'message':"The Election is closed.Please contact administrator for more details.",'messageTitle':"E-Voting"})
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
					return render_to_response('messages.html',{'message':"You have successfully created Good and Evil Passphrases!!!",'messageTitle':"E-Voting"})
				if voter:
					return render_to_response('messages.html',{'message':"You already have created both passphrases!!!",'messageTitle':"E-Voting"})
			
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
					return HttpResponseRedirect('/home')

				else:
					return HttpResponseRedirect('/home')
			else:
				return HttpResponseRedirect('/home')

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
		return HttpResponseRedirect('/administrator')

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
		return HttpResponseRedirect('/administrator')

#This function is used to send mail to person to_username with the email id to_user_email to confirm  the support for person named for_username

def verifySupport(request,hashedKey):
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
			candidate = CandidatesList.objects.get(candidatesRollNo = candidatesRollno)
			candidate.secondSupportersSupport = 1
			candidate.save()
			return render_to_response('thanksmessage.html',{'candidatesName':candidate.candidatesName,'supportersName':candidate.secondSupporter,'position':candidate.position,'hostel':candidate.hostel})
		else:
			return render_to_response('messages.html',{'message':"Sorry,some error occured.You are not a supporter of "+ candidate.candidatesName,'messageTitle':"E-Voting"})
	if supporter1:
		candidatesRollno = supporter1.candidatesRollNo
		candidate = CandidatesList.objects.get(candidatesRollNo = candidatesRollno)
		candidate.firstSupportersSupport = 1
		candidate.save()
		return render_to_response('thanksmessage.html',{'candidatesName':candidate.candidatesName,'supportersName':candidate.secondSupporter,'position':candidate.position,'hostel':candidate.hostel})

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
	if 'adminUsername' in request.session:
		#to be completed....
		maxVotes = -1
		allHostels = ListOfHostel.objects.all()
		#return HttpResponse(allHostels)
		for hostel in allHostels:
			listOfPositions = PostsForElection.objects.all().filter(hostelsName = hostel.hostelsName)
			#return HttpResponse(listOfPositions)
			for position in listOfPositions:
				maxVotes = -1
				listOfNominees = ListOfNominee.objects.all().filter(hostel = hostel.hostelsName,position = position.position)
				#return HttpResponse(listOfNominees)
				for nominee in listOfNominees:
					try:
						votes = Ballot.objects.all().filter(hostel = hostel.hostelsName,position = position.position,nomineeSelected = nominee.nomineesName)
						#return HttpResponse(votes)
					except Ballot.DoesNotExist:
						votes = 0
					noOfVotes = votes.count()
					#return HttpResponse(noOfVotes)
					nominee.NumberOfVotes = noOfVotes
					nominee.save()
					if noOfVotes > maxVotes:
						name = nominee.nomineesName
						roll = nominee.nomineesRollNo
						maxVotes = noOfVotes
				#return HttpResponse(maxVotes)
				try:
					sec = ListOfSecretary.objects.get(hostelsName = hostel.hostelsName,position = position.position,nameOfSecretary = name,rollNoOfSecretary = roll)
				except ListOfSecretary.DoesNotExist:
					sec = None
				if not sec:
					#return HttpResponse("hello")
					secretary = ListOfSecretary(hostelsName = hostel.hostelsName,position = position.position,nameOfSecretary = name,rollNoOfSecretary = roll)
					secretary.save()
		return render_to_response('adminMessages.html',{'message':'Successfully counted the votes!!!','messageTitle':"E-Voting"})
	else:
		return HttpResponseRedirect('EVoting/admin')

def viewNominees(request):
	if 'username' in request.session:
		listOfNominees = ListOfNominee.objects.all()
		if listOfNominees.count() == 0:
			return render_to_response('messages.html',{'message':"The final list of Nominee's is not yet prepared",'messageTitle':"E-Voting"})
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
			return render_to_response('messages.html',{'message':"The votes are not yet counted",'messageTitle':"E-Voting"})
		elif finalList.count() != 0:
			List = []
			for sec in finalList:
				List.append({'hostel' : sec.hostelsName.upper(),'position':sec.position.upper(),'name':sec.nameOfSecretary.upper(),'rollno':sec.rollNoOfSecretary})
			return render_to_response('ListOfSecretaries.html',{'List':List})

	else:
		return HttpResponseRedirect('/login')

def aboutNominee(request,nomineesRollno):
	if 'username' in request.session:
		return HttpResponse("Hello " + nomineesRollno)
		
	else:
		return HttpResponseRedirect('/login')


def registerUsers(request):
	if 'adminUsername' in request.session:
		listOfHostels  = ListOfHostel.objects.all()
		hostels = []
		for i in range(listOfHostels.count()):
			hostels.append(listOfHostels[i].hostelsName)
		return render_to_response('usersRegistration.html',{'hostels':hostels})
	else:
		return HttpResponseRedirect('/administrator')

def checkValidUsers(request):
	if 'adminUsername' in request.session:
		rollno = request.POST['rollno']
		username = request.POST['username']
		hostel = request.POST['hostel']
		password = request.POST['password1']
		email = request.POST['email']
		user = UserList(rollNumber = rollno,username=username,password=password,hostelAlloted=hostel,emailId=email)
		user.save()
		return HttpResponse('messages.html',{'message':"The user's data has been stored",'messageTitle':"H-RAM"})

	else:
		return HttpResponseRedirect('/administrator')

def checkIfVoteCounted(request):
	if 'username' in request.session:
		rollno = request.session['member_id']
		try:
			user = UserList.objects.get(rollNumber = rollno)
		except UserList.DoesNotExist:
			user = None
		if user:
			try:
				voter = VotersList.objects.get(voterDetails = user)
			except VotersList.DoesNotExist:
				voter = None
			if voter:
				try:
					voted = Ballot.objects.all().filter(voter = voter)
				except Ballot.DoesNotExist:
					voted = None
				if voted.count() != 0:
					return render_to_response('messages.html',{'message':"You vote has been counted!!!"})
				else:
					return render_to_response('messages.html',{'message':"Your vote is not counted"})
			if not voter:
				return render_to_response('messages.html',{'message':"You are not eligible to vote as you have not yet created the two passwords"})
		if not user:
			return render_to_response('messages.html',{'message':"You are not a valid user"})
	else:
		return HttpResponseRedirect('/login')



