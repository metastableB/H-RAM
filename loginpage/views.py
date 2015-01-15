from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from django.core.context_processors import csrf
from loginpage.models import Post

def register(request):
	#for register
	return render_to_response('register.html')

def home(request):
	return render_to_response('home.html')

def check(request):
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
			usr = Post.objects.get(username='username')
		except Post.DoesNotExist:
			usr = None
		if not usr:
			pass1 = request.POST['pass1']
			if (pass1==0):
				errors.append("Please enter a password")
			if (len(pass1)!=5):
				errors.append("password is not of length 5")
				validpass1=False
			else:
				validpass1=True
			pass2=request.POST['pass2']

			if (pass2==0):
				errors.append("Please enter a password")
			if (len(pass2)!=5):
				errors.append("Confirm password is not of length 5")
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

def check_signin(request):
	if request.method == 'POST':
		incorrect = "Incorrect Password"
		errors=[]
		valid = False
		validuser = False
		validpass=False
		username = request.POST['username']
		if (len(username)!=0):
			validuser=True
		else:
			errors.append("Please enter a username.")

		password = request.POST['paswrd']
		if (len(password)!=0):
			validpass=True
		else:
			errors.append("Please enter a password.")
		if(validpass&validuser):
			try:
				usr = Post.objects.get(username=username)
			except Post.DoesNotExist:
				usr = None

			if (usr):
				if(password == usr.password):
					valid=True

				if(valid):
					count=usr.count
					usr.count=count+1
					count=count+1
					usr.save()
					return render_to_response('profile.html',{'username':username,'count':count})
				else:
					errors.append("Password is incorrect.")
					return render_to_response('signin.html',{'errors':errors})
			if not usr:
				return render_to_response('failure.html',{'msg':"Please register and then log in"})
		else:
			return render_to_response('signin.html',{'errors':errors})
	else:
		return render_to_response('signin.html')




def signin(request):
	return render_to_response('signin.html')





# Create your views here.
