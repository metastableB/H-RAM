from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList,RoomList,FriendsPreference
from django.db.models import Max
import random
import allocation

def register(request):
	#for register
	return render_to_response('register.html')

def friendsprefrence(request):
	#for friends prefrence list
	if 'username' in request.session:
		return render_to_response('friendspref.html')
	else :
		return HttpResponseRedirect('/login')

def home(request):
	#return render_to_response('home.html')
	if 'username' in request.session:
		return render_to_response('home.html')
	else :
		return HttpResponseRedirect('/login')

def recordFriendsPreference(request):
	if 'username' in request.session:
		errors = []
		username = request.session['username']
		rollNumber = request.session['member_id']
		userDetails = UserList.objects.get(username = username)
		#user = FriendsPreference(uId = userDetails)
		friend1 = request.POST['friend1']
		checkFriend1 = UserList.objects.get(rollNumber = friend1)
		if not checkFriend1:
			errors.append("Enter a valid first friend")
			return render_to_response('friendspref.html',{'errors':errors})
		friend2 = request.POST['friend2']
		checkFriend2 = UserList.objects.get(rollNumber = friend2)
		if not checkFriend2:
			errors.append("Enter a valid second friend")
			return render_to_response('friendspref.html',{'errors':errors})

		friend3 = request.POST['friend3']
		checkFriend3 = UserList.objects.get(rollNumber = friend3)
		if not checkFriend3:
			errors.append("Enter a valid third friend")
			return render_to_response('friendspref.html',{'errors':errors})

		friend4 = request.POST['friend4']
		checkFriend4 = UserList.objects.get(rollNumber = friend4)
		if not checkFriend4:
			errors.append("Enter a valid fourth friend")
			return render_to_response('friendspref.html',{'errors':errors})

		friend5 = request.POST['friend5']
		checkFriend5 = UserList.objects.get(rollNumber = friend5)
		if not checkFriend5:
			errors.append("Enter a valid fifth friend")
			return render_to_response('friendspref.html',{'errors':errors})
		newuser = FriendsPreference(uId = userDetails,rollNumber = rollNumber ,preferedfriendUId1 = friend1,preferedfriendUId2 = friend2,preferedfriendUId3 = friend3,preferedfriendUId4 = friend4,preferedfriendUId5 = friend5)
		newuser.save()
		errors = []
		errors.append("Your preferences have been saved")
		return render_to_response('home.html',{'errors' : errors})

		'''user.preferedfriendUId1 = friend1
		user.preferedfriendUId2 = friend2
		user.preferedfriendUId3 = friend3
		user.preferedfriendUId4 = friend4
		user.preferedfriendUId4 = friend5'''


	else:
		return HttpResponseRedirect('/login')

def access(request):
	return render_to_response('access.html')

def openGrid(request):
	return render_to_response('tables.html')

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

		return render_to_response('home.html',{'errors' : preferenceOrder})
	else:
		return render_to_response('success.html')

def test(request):
	return render_to_response('testing.html')

def floorPlan(request):
	return render_to_response('floors.html')

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
			errors.append("Please enter a username.")
			
		password = request.POST['paswrd']
		if (len(password)!=0):
			validpassword=True
		else:
			errors.append("Please enter a password.")
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
					errors.append("Password is incorrect.")
					return render_to_response('login.html',{'errors':errors})
			if not user:
				errors.append("Please Enter the correct credentials.")
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
	if 'username' in request.session:
		try:
			del request.session['member_id']
			del request.session['username']
		except keyError:
			pass
		return HttpResponseRedirect('/login')
	else :
		return HttpResponseRedirect('/login')

	#return HttpResponse("You are looged out!!!")

'''def checkIfloggedIn(request):
	if 'username' in request.session:
		return True
	return False'''

def login(request):
	return render_to_response('login.html')

def allocationMethod(request):
	preference = 1
	maxPreference =  RoomPreference.objects.all().aggregate(Max('preferenceNumber'))
	for preference in range(1,10):
		iThPreferences = RoomPreference.objects.all().filter(preferenceNumber = preference, valid = 1)
		# updating counter
		for tempPreference in iThPreferences:
			roomNo = tempPreference.preferedRoom
			allocFlag = RoomList.objects.get(roomNumber = roomNo)
			if allocFlag.counter != -1 :
				temp = allocFlag.counter 
				temp += 1
				toSave = RoomList.objects.get(roomNumber = roomNo)
				toSave.counter = temp
				toSave.save()
		allocation.sortAllocate(preference)
	return render_to_response('home.html')
'''
def makeRoomList(request):
	roomno =1;
	for roomno in range(32):
		newRoom1 = RoomList(roomNumber = roomno+100 ,)

		newroom = RoomPreference(uId = userDetails ,rollNumber = userDetails.rollNumber ,preferenceNumber=j+lastPreference+1,preferedRoom=preferenceOrder[j])
			newroom.save()	
	floor = models.CharField(max_length = 5)
	#wing = models.CharField(max_length = 5)
	uId = models.ForeignKey(UserList)
	count = models.IntegerField(max_length = 4 , default = 0)
	x = models.IntegerField(max_length = 3)
	y = models.IntegerField(max_length = 3)
'''

