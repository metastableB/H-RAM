from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList,RoomList,FriendsPreference,StudentBioDataTable,GlobalFlag,SuperGlobalFlag,RoomAllocationResults
from django.db.models import Max

from .forms import FriendsPreferenceForm
import random
import allocation

def register(request):
	#for register
	return render_to_response('register.html')

def friendsprefrence(request):
	#for friends prefrence list
	if 'username' in request.session:
		rollNumber = request.session['member_id']
		try :
			allocationDone = SuperGlobalFlag.objects.get()
		except SuperGlobalFlag.DoesNotExist:
			allocationDone = None
		if allocationDone and allocationDone.allocationFinished == 1 :
			friendsList = FriendsPreference.objects.get(rollNumber = rollNumber)
			results = []
			friend1 = friendsList.preferedfriendUId1
			friend2 = friendsList.preferedfriendUId2
			friend3 = friendsList.preferedfriendUId3
			friend4 = friendsList.preferedfriendUId4 
			friend5 = friendsList.preferedfriendUId5
			results.append("#1 " + friend1)
			results.append("#2 " + friend2)
			results.append("#3 " + friend3)
			results.append("#4 " + friend4)
			results.append("#5 " + friend5)
			return render_to_response('friendPreferenceList.html',{'results' : results})

		try :
			friendsList = FriendsPreference.objects.get(rollNumber = rollNumber)
		except FriendsPreference.DoesNotExist:
			friendsList = None
		if friendsList :
			friend1 = friendsList.preferedfriendUId1
			friend2 = friendsList.preferedfriendUId2
			friend3 = friendsList.preferedfriendUId3
			friend4 = friendsList.preferedfriendUId4 
			friend5 = friendsList.preferedfriendUId5
			return render_to_response('friendspref.html',{'friend1':friend1,'friend2':friend2,'friend3':friend3,'friend4':friend4,'friend5':friend5})
		return render_to_response('friendspref.html')
	else :
		return HttpResponseRedirect('/login')

def myprofile(request):
	#for friends prefrence list
	if 'username' in request.session:
		username = request.session['username']
		rollNumber = request.session['member_id']
		biodata = StudentBioDataTable.objects.get(rollNumber = rollNumber)
		jeeAIR = biodata.jeeAIR
		name = biodata.name
		roll = biodata.rollNumber
		dept = biodata.courseAdmitted
		sex = biodata.gender
		hostel = biodata.hostelAlloted
		dob = biodata.dateOfBirth
		category = biodata.category
		fname = biodata.fathersName
		income = biodata.parentsOrGuardiansAnnualIncom
		mailingAddress = biodata.mailingAddress
		permanentAddress = biodata.permanentAddress
		motherTongue = biodata.motherTongue
		nationality = biodata.nationality
		nativeState = biodata.nativeState

		return render_to_response('myprofile.html',{'roll':roll,'jeeAIR':jeeAIR,'name':name,'dept':dept,'sex':sex,'hostel':hostel,'dob':dob,'category':category,'fname':fname,'income':income,'mailingAddress':mailingAddress,'permanentAddress':permanentAddress,'motherTongue':motherTongue,'nationality':nationality,'nativeState':nativeState})

	else :
		return HttpResponseRedirect('/login')

def changepassword(request):
	if 'username' in request.session:
		return render_to_response('changepassword.html')
	else :
		return HttpResponseRedirect('/login')

def home(request):
	#return render_to_response('home.html')
	if 'username' in request.session:
		return render_to_response('home.html')
	else :
		return HttpResponseRedirect('/login')

#---------------------------------
#def friendsprefrence(request):
    # if this is a POST request we need to process the form data
 #   if request.method == 'POST':
        # create a form instance and populate it with data from the request:
  #      form = FriendsPreferenceForm(request.POST)
   #     return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
  #  else:
   #     form = FriendsPreferenceForm()

    #return render(request, 'friendspref.html', {'form': form})
  #--------------------------------------------		

def recordFriendsPreference(request):
	if 'username' in request.session:
		errors = []
		username = request.session['username']
		rollNumber = request.session['member_id']
		userDetails = UserList.objects.get(username = username)
		#user = FriendsPreference(uId = userDetails)
	
		friend1 = request.POST['friend1']
		try :
			checkFriend1 = UserList.objects.get(rollNumber = friend1)
		except UserList.DoesNotExist:
			checkFriend1 = None 
		if not checkFriend1:
			errors.append("Enter a valid first friend")
			return render_to_response('friendspref.html',{'errors':errors})
	
		friend2 = request.POST['friend2']
		try :
			checkFriend2 = UserList.objects.get(rollNumber = friend2)
		except UserList.DoesNotExist:
			checkFriend2 = None 
		if not checkFriend2:
			errors.append("Enter a valid second friend")
			return render_to_response('friendspref.html',{'errors':errors})
		elif friend1 == friend2 :
			errors.append("You cannot enter duplicate values. Try again.")
			return render_to_response('friendspref.html',{'errors':errors})

		friend3 = request.POST['friend3']
		try :
			checkFriend3 = UserList.objects.get(rollNumber = friend3)
		except UserList.DoesNotExist:
			checkFriend3 = None 
		if not checkFriend3:
			errors.append("Enter a valid third friend")
			return render_to_response('friendspref.html',{'errors':errors})
		elif friend1 == friend3 or friend2 == friend3:
			errors.append("You cannot enter duplicate values. Try again.")
			return render_to_response('friendspref.html',{'errors':errors})

		friend4 = request.POST['friend4']
		try :
			checkFriend4 = UserList.objects.get(rollNumber = friend4)
		except UserList.DoesNotExist:
			checkFriend4 = None 
		if not checkFriend4:
			errors.append("Enter a valid fourth friend")
			return render_to_response('friendspref.html',{'errors':errors})
		elif friend1 == friend4 or friend2 == friend4 or friend3 == friend4:
			errors.append("You cannot enter duplicate values. Try again.")
			return render_to_response('friendspref.html',{'errors':errors})

		friend5 = request.POST['friend5']
		try :
			checkFriend5 = UserList.objects.get(rollNumber = friend5)
		except UserList.DoesNotExist:
			checkFriend5 = None 
		if not checkFriend5:
			errors.append("Enter a valid fifth friend")
			return render_to_response('friendspref.html',{'errors':errors})
		elif friend1 == friend5 or friend2 == friend5 or friend3 == friend5 or friend4 == friend5:
			errors.append("You cannot enter duplicate values. Try again.")
			return render_to_response('friendspref.html',{'errors':errors})

		if friend1 == rollNumber or friend2 == rollNumber or friend3 == rollNumber or friend4 == rollNumber or friend5 == rollNumber :
			errors.append("You cannot enter your own roll-number. Try again.")
			return render_to_response('friendspref.html',{'errors':errors})

		try:
			userObject = FriendsPreference.objects.get(rollNumber = rollNumber)
		except FriendsPreference.DoesNotExist:
			userObject = None
		if not userObject:
			newuser = FriendsPreference(uId = userDetails,rollNumber = rollNumber ,preferedfriendUId1 = friend1,preferedfriendUId2 = friend2,preferedfriendUId3 = friend3,preferedfriendUId4 = friend4,preferedfriendUId5 = friend5)
			newuser.save()
			errors = []
			errors.append("Your preferences have been saved")
		if userObject:
			#newuser = FriendsPreference(uId = userDetails,rollNumber = rollNumber ,preferedfriendUId1 = friend1,preferedfriendUId2 = friend2,preferedfriendUId3 = friend3,preferedfriendUId4 = friend4,preferedfriendUId5 = friend5)
			#newuser.save()
			userObject.uId = userDetails
			userObject.rollNumber = rollNumber
			userObject.preferedfriendUId1 = friend1
			userObject.preferedfriendUId2 = friend2
			userObject.preferedfriendUId3 = friend3
			userObject.preferedfriendUId4 = friend4
			userObject.preferedfriendUId5 = friend5
			userObject.save()
			errors = []
			errors.append("Your preferences have been saved")
		return render_to_response('home.html',{'errors' : errors})

	else:
		return HttpResponseRedirect('/login')

def access(request):
	if 'username' in request.session:
		return render_to_response('access.html')
	else :
		return HttpResponseRedirect('/login')

def openGrid(request):
	if 'username' in request.session:
		return render_to_response('tables.html')
	else :
		return HttpResponseRedirect('/login')

def bookRoom(request):
	if 'username' in request.session:
		logInUsername = request.session['username']
		preferenceList = request.POST['preference']
		userDetails = UserList.objects.get(username = logInUsername)
		userRoomPreference = RoomPreference.objects.all().filter(uId = userDetails.uniqueId)
		if userRoomPreference.count () > 0 :
	 		userRoomPreference = userRoomPreference.order_by('-preferenceNumber')[0]	
	 		lastPreference = userRoomPreference.preferenceNumber
		else:
	 		lastPreference = 0
	 		userRoomPreference = None
		i = 0 
		temp = ""
		preferenceOrder = []
		for char in preferenceList:
			if(char != ","):
				temp += char
			elif(char == ","):
				preferenceOrder.append(temp)
				temp = ""
				i += 1
		preferenceOrder.append(temp)						#As the last room in the preference was not getting into the array.
		j=0
		for j in range(len(preferenceOrder)) :
			newroom = RoomPreference(uId = userDetails ,rollNumber = userDetails.rollNumber ,preferenceNumber=j+lastPreference+1,preferedRoom=preferenceOrder[j])
			newroom.save()
		if j != 0 :
			userFlag = GlobalFlag(uId = userDetails ,rollNumber = userDetails.rollNumber,roomPreferencesSelected = 1)
			userFlag.save()

		return render_to_response('home.html',{'errors' : preferenceOrder})
	else:
		return HttpResponseRedirect('/login')

def test(request):
	return render_to_response('testing.html')

def floorPlan(request):
	if 'username' in request.session:
		username = request.session['username']
		rollNumber = request.session['member_id']
		userDetails = UserList.objects.get(username = username)
		try:
			userFlag = GlobalFlag.objects.get(rollNumber = rollNumber)
		except GlobalFlag.DoesNotExist:
			userFlag = None
		if not userFlag:
			return render_to_response('floors.html')
		else :
			roomPreferenceList = RoomPreference.objects.all().filter(rollNumber = rollNumber)
			results = []
			for i in range(roomPreferenceList.count()):
				results.append(roomPreferenceList[i].rollNumber + "  " + roomPreferenceList[i].preferedRoom) 
			return render_to_response('roomPreferenceList.html',{'results' : results})
	else :
		return HttpResponseRedirect('/login')

def messages(request):
	if 'username' in request.session:
		return render_to_response('messages.html')
	else :
		return HttpResponseRedirect('/login')
	

'''def check(request):
	if request.method=="POST":
		errors=[]
		validUsername = False
		validPassword = False
		valid=False
		username = request.POST['username']
		if (len(username) != 0):
			if(len(username)<128):
				validUsername=True
			else:
				errors.append("Please enter a username less than 128 characters")
		else:
			errors.append("Please enter username")
		
		try:
			usr = Post.objects.get(username=username)
		except Post.DoesNotExist:
			usr = None
		if not usr:
			pass1 = request.POST['pass1']	
			
			if (len(pass1)!=5):
				if(len(pass1)==0):
					validpass1=True
				else:
					errors.append("password is not of length 5")
					validpass1=False
			else:
				validpass1=True
			pass2=request.POST['pass2']
		
			
			if (len(pass2)!=5):
				if(len(pass2)==0):
					validpass2=True
				else:
					errors.append("password is not of length 5")
					validpass2=False
			else:
				validpass2=True

			if (pass1 != pass2):
				errors.append("Two password didn't match")
			else:
				if(validpass1 & validpass2):
					validPassword=True
		if(usr):
			errors.append("Username already exists.Please enter something else")
		if(validUsername&validPassword):
			valid=True
		if (valid):
			newUser= Post(username=username,password=pass1,count='0')
			newUser.save()
			return render_to_response('success.html',{'valid' : valid})
		else:
			return render_to_response('register.html',{'errors':errors})
	else:
		return render_to_response('register.html')
'''
def validate(request):
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
			errors.append("Please enter  username.")
			
		password = request.POST['paswrd']
		if (len(password)!=0):
			validpassword=True
		else:
			errors.append("Please enter  password.")
		if(validpassword & validuser):			
			try:
				user = UserList.objects.get(username=username)
			except UserList.DoesNotExist:
				user = None

			if (user):
				if(password == user.password):
					valid=True

				if(valid):
					request.session['member_id'] = user.rollNumber
					request.session['username'] = user.username
					return HttpResponseRedirect('/home')
				else:
					errors.append("Incorrect password. Please try again.")
					return render_to_response('login.html',{'errors':errors})
			if not user:
 				errors.append("Please enter correct credentials")
				return render_to_response('login.html',{'errors':errors})
		else:
			return render_to_response('login.html',{'errors':errors})
	else:
		return render_to_response('login.html')

def profile(request):
	if 'username' in request.session:
		user = request.session['username']
		return render_to_response('profile.html',{'username':user})
	return HttpResponseRedirect('/login')

def logout(request):
	errors =[]
	if 'username' in request.session:
		try:
			del request.session['member_id']
			del request.session['username']
		except keyError:
			pass
		#return HttpResponseRedirect('/login')
		errors.append("You have sucessfully logged out.")
		return render_to_response('login.html',{'errors':errors})
	else :
		errors.append("You are not logged in.")
		return render_to_response('login.html',{'errors':errors})

	#return HttpResponse("You are looged out!!!")

'''def checkIfloggedIn(request):
	if 'username' in request.session:
		return True
	return False'''

def login(request):
	if 'username' in request.session:
		return HttpResponseRedirect('/home')
	return render_to_response('login.html')

### Allocation Algorithm
# RoomPreference table holds objects of each room preference by each users
# For each preference number starting from 1
# Update the room count to indicate no of people who has that room in the current
# preference 
# After all the rooms for the current preference number has been updated allocate rooms

def allocationMethod(request):
	try :	
		sGFlag = SuperGlobalFlag.objects.get()
	except SuperGlobalFlag.DoesNotExist:
		sGFlag = None
	if  sGFlag and sGFlag.allocationFinished == 1 :
		roomAllocationList = RoomAllocationResults.objects.all()
		results = []
		for room in roomAllocationList:
			results.append(room.rollNumber + "      " + room.roomNumber) 
		return render_to_response('allocationResults.html',{'results' : results})
	errors = []
	preference = 1
	maxPreference =  RoomPreference.objects.all().aggregate(Max('preferenceNumber'))
	for preference in range(1,10):
		iThPreferences = RoomPreference.objects.all().filter(preferenceNumber = preference, valid = 1)
		# updating counter
		#return HttpResponse("incrementing2")
		for tempPreference in iThPreferences:
			#return HttpResponse("incrementing1")
			roomNo = tempPreference.preferedRoom
			allocFlag = RoomList.objects.get(roomNumber = roomNo)
			#errors.append(allocFlag.rollNumber)
			#return render_to_response('login.html',{'errors':errors})
			if allocFlag.rollNumber == "-1" :
				temp = allocFlag.counter 
				temp = temp + 1
				allocFlag.counter = temp

				allocFlag.save()
				
		allocation.sortAllocate(preference)		

	# Create a DB table and not a dynamic shit
	results = []	
	resultList = RoomList.objects.all().filter(counter = -1)
	for i in range(resultList.count()):
		tempResult = RoomAllocationResults(roomNumber = resultList[i].roomNumber , rollNumber = resultList[i].rollNumber)
		tempResult.save()

	try :	
		sGFlag = SuperGlobalFlag.objects.get()
	except SuperGlobalFlag.DoesNotExist:
		sGFlag = None

	if sGFlag:
		sGFlag.allocationFinished = 1
	else :
		sGFlag = SuperGlobalFlag(allocationFinished = 1)
	sGFlag.save()
	
	roomAllocationList = RoomAllocationResults.objects.all()
	results = []
	for room in roomAllocationList:
		results.append(room.rollNumber + "      " + room.roomNumber) 
	
	return render_to_response('allocationResults.html',{'results' : results})
	#return render_to_response('allocationResults.html',{'results' : results})
	#return HttpResponse("success")

def fetchAllocationResults():
	
	roomAllocationList = RoomAllocationResults.objects.all()
	results = []
	
	return render_to_response('allocationResults.html',{'results' : results})
	for room in roomAllocationList:
		results.append(room.rollNumber + "      " + room.roomNumber) 

	return render_to_response('allocationResults.html',{'results' : results})

def about(request):
	return render_to_response('about.html')


def contact(request):
	return render_to_response('contact.html')