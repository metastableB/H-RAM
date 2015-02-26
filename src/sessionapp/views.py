from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList

def register(request):
	#for register
	return render_to_response('register.html')

def home(request):
	return render_to_response('home.html')

def access(request):
	return render_to_response('access.html')

def openGrid(request):
	return render_to_response('tables.html')

def bookRoom(request):
	#request.method=="POST"
	#roomNumber= request.POST['roomNumber']
	roomnumber = []
	error = []
	i = 0
	if 'username' in request.session:
		request.method=="POST"
		error.append(request.POST['first'])
		error.append(request.POST['second'])
		error.append(request.POST['third'])
		error.append(request.POST['fourth'])
		error.append(request.POST['fifth'])
		error.append(request.POST['sixth'])
		error.append(request.POST['seventh'])
		error.append(request.POST['eight'])
		error.append(request.POST['nineth'])
		if(request.POST["first"] != "-1"):
		
			roomnumber.append(request.POST['first'])
			i = i+1
		if(request.POST['second'] != '-1'):
		
			roomnumber.append(request.POST['second'])
			i = i+1
		if(request.POST['third'] != '-1'):
		#else:
			roomnumber.append(request.POST['third'])
			i = i+1
		if(request.POST['fourth'] != '-1'):
			roomnumber.append(request.POST['fourth'])
			i = i+1
		if(request.POST['fifth'] != '-1'):
		#else:
			roomnumber.append(request.POST['fifth'])
			i = i+1
		if(request.POST['sixth'] != '-1'):
		#else:
			roomnumber.append(request.POST['sixth'])
			i = i+1
		if(request.POST['seventh'] != '-1'):
		#else:
			roomnumber.append(request.POST['seventh'])
			i = i+1
		if(request.POST['eight'] != '-1'):
		#else:
			roomnumber.append(request.POST['eight'])
			i = i+1
		if(request.POST['nineth'] != '-1'):
		#else:
			roomnumber.append(request.POST['nineth'])
			i = i+1
		j=0
		error.append(i)
		for j in range(i-1):
			newroom = RoomPreference(preferenceNumber = 2,preferedRoom = '305')
			newroom.save()
			j += 1
		#newroom= RoomPreference(preferenceNumber="1",preferedRoom=roomNumber)
		#newroom.save()
		return render_to_response('home.html',{'errors' : error})
	
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
		if(validpassword&validuser):			
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
					return render_to_response('signin.html',{'errors':errors})
			if not user:
				return render_to_response('failure.html',{'msg':"Please register and then log in"})
		else:
			return render_to_response('signin.html',{'errors':errors})
	else:
		return render_to_response('signin.html')

def profile(request):
	if 'username' in request.session:
		user = request.session['username']
		return render_to_response('profile.html',{'username':user})
	return HttpResponseRedirect('/signin')

def logout(request):
	try:
		del request.session['member_id']
		del request.session['username']
	except keyError:
		pass
	return HttpResponseRedirect('/signin')
	#return HttpResponse("You are looged out!!!")

'''def checkIfloggedIn(request):
	if 'username' in request.session:
		return True
	return False'''

def signin(request):
	return render_to_response('signin.html')






