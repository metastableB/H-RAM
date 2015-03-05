from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList
from django.db.models import Max

def register(request):
	#for register
	return render_to_response('register.html')

def home(request):
	#return render_to_response('home.html')
	if 'username' in request.session:
		return render_to_response('home.html')
	else :
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
				return render_to_response('failure.html'.html,{'msg':"Please Enter the correct credentials"})
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






