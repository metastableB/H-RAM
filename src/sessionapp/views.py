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
	return render_to_response('home.html')

def access(request):
	return render_to_response('access.html')

def bookRoom(request):
	# TODO : Deal with this
	#request.method == "POST"
	if 'username' in request.session:
		logInUsername = request.session['username']
		userDetails = UserList.objects.get(username = logInUsername)
	 	userRoomPreference = RoomPreference.objects.all().filter(uId = userDetails.uniqueId)
	 	if userRoomPreference.count () > 0 :
	 		userRoomPreference = userRoomPreference.order_by('-preferenceNumber')[0]	
	 		userRoomPreferenceNumber = userRoomPreference.preferenceNumber
	 	else:
	 		userRoomPreferenceNumber = 0
	 		userRoomPreference = None
	 		
	 	userRoomPreferenceNumber = userRoomPreferenceNumber + 1	
		newRoomPreference = RoomPreference(uId = userDetails ,rollNumber = userDetails.rollNumber,
			preferenceNumber = userRoomPreferenceNumber ,preferedRoom = "301")
		newRoomPreference.save()
		return render_to_response('home.html')
	
	return render_to_response('success.html')

def test(request):
	return render_to_response('testing.html')

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
					return HttpResponseRedirect('/profilePage')
				else:
					errors.append("Password is incorrect.")
					return render_to_response('login.html',{'errors':errors})
			if not user:
				return render_to_response('failure.html',{'msg':"Please register and then log in"})
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
	try:
		del request.session['member_id']
		del request.session['username']
	except keyError:
		pass
	return HttpResponseRedirect('/login')
	#return HttpResponse("You are looged out!!!")

'''def checkIfloggedIn(request):
	if 'username' in request.session:
		return True
	return False'''

def login(request):
	return render_to_response('login.html')






