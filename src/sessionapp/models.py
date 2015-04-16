from django.db import models

class UserList(models.Model):
    uniqueId = models.AutoField(primary_key = True)
    rollNumber = models.CharField(max_length = 10)
    username = models.CharField(max_length = 30)
    # TODO : use SHA-1 hash function
    password = models.CharField(max_length = 64)
    emailId = models.EmailField(max_length = 254)
    # for temporary purpose created hostel in userlist
    hostelAlloted = models.CharField(max_length = 30)
    def  __unicode__ (self):
    	return self.username

class AdminDetail(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 64)

class FriendsPreference(models.Model):
    uId = models.ForeignKey(UserList)
    rollNumber = models.CharField(max_length = 10)
    # TODO : whether to store userId or rollnumber of the friend
    preferedfriendUId1 = models.CharField(max_length = 10 , default = "Roll Number")
    preferedfriendUId2 = models.CharField(max_length = 10 , default = "Roll Number")
    preferedfriendUId3 = models.CharField(max_length = 10 , default = "Roll Number")
    preferedfriendUId4 = models.CharField(max_length = 10 , default = "Roll Number")
    preferedfriendUId5 = models.CharField(max_length = 10 , default = "Roll Number")
    def  __unicode__ (self):
    	return u'%s' %(self.uId)

class RoomPreference(models.Model):
    # Each UId will have a correspinding set of entries in the table
    # when quieried for a UId this will return a list which acts 
    # as a sub-table of sorts for each user
    uId = models.ForeignKey(UserList)
    rollNumber = models.CharField(max_length = 10)
    preferenceNumber = models.IntegerField(max_length = 3)
    preferedRoom = models.CharField(max_length = 4)
    valid = models.IntegerField(max_length = 1, default = 1)

    def  __unicode__ (self):
    	return u'%10s: %-5s %-5s' %(self.uId,self.preferenceNumber,self.preferedRoom)

class RoomList(models.Model):
	# Holds information regarding each room
	roomNumber = models.CharField(max_length = 5)
	rollNumber = models.CharField(max_length = 10,default = '-1')
	floor = models.CharField(max_length = 5)
	#wing = models.CharField(max_length = 5)
	#uId = models.ForeignKey(UserList)
	counter = models.IntegerField(max_length = 4 , default = 0)
	x = models.IntegerField(max_length = 3)
	y = models.IntegerField(max_length = 3)
	def __unicode__ (self):
		return u'%10s %10s (x,y) %d %d counter %d'%(self.roomNumber,self.rollNumber,self.x,self.y,self.counter)

class StudentBioDataTable(models.Model):
	uId = models.ForeignKey(UserList)
	rollNumber =  models.CharField(max_length=10)

	# Introduction
	# TODO : Restrict this field
	#jeeRegistrationNo = models.CharField(max_length = 10)
	jeeAIR = models.IntegerField(max_length = 7)
	name = models.CharField(max_length = 50)
	hostelAlloted = models.CharField(max_length = 50)
	courseAdmitted = models.CharField(max_length = 50)

	# Physical
	dateOfBirth = models.CharField(max_length = 10)
	# M F O
	gender = models.CharField(max_length = 1)
	#bloodGroup = models.CharField(max_length = 3)
	# TODO : give a buttonBox
	#height = models.IntegerField(max_length = 3)
	#weight = models.IntegerField(max_length = 3)
	category = models.CharField(max_length = 20) 
	#cast = models.CharField(max_length = 20)
	#religion = models.CharField(max_length = 20)

	# Parental 
	fathersName = models.CharField(max_length = 50)
	#guardiansName = models.CharField(max_length = 50)
	#guardiansProfession = models.CharField(max_length = 50)
	# TODO : Give button box
	parentsOrGuardiansAnnualIncom = models.IntegerField(max_length = 3)

	# Residiantial
	areaBelongingTo = models.CharField(max_length = 50)
	mailingAddress = models.CharField(max_length = 150)
	# TODO : Check for international pin
	#mailingPin =  models.IntegerField(max_length = 7)
	# TODO : phone number size
	#mailingTelephone =  models.IntegerField(max_length = 11)
	#mailingMobile =  models.IntegerField(max_length = 11)
	#mailingPoliceStation = models.CharField(max_length = 50)

	permanentAddress =  models.CharField(max_length = 150)
	#permanentPin =  models.IntegerField(max_length = 7)
	#permanentTelephone = models.IntegerField(max_length = 11)
	#permanentMobile =  models.IntegerField(max_length = 11)
	#permanentPoliceStation = models.CharField(max_length = 50)
	
	motherTongue = models.CharField(max_length = 20)
	nationality = models.CharField(max_length = 20)

	#If indian
	nativeState = models.CharField(max_length = 20)
	#TODO : passpostNo dataType (If not indian)
	#passportNo =  models.IntegerField(max_length = 7)

	# Educational
	#qualifyingExam = models.CharField(max_length = 50)
	#qualifyingYear =  models.IntegerField(max_length = 7)
	#qualifyingBoard = models.CharField(max_length = 50)
	#qualifyingPercentageMarks =  models.IntegerField(max_length = 7)
	def  __unicode__ (self):
		return u'%s' %(self.uId)
