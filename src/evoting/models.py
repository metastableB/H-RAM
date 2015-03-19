from django.db import models
from sessionapp.models import UserList
#List of all candidates who want to contest in the election
class CandidatesList(models.Model):
	candidatesName  = models.CharField(max_length = 60)
	candidatesRollNo  = models.CharField(max_length = 10)
	hostel = models.CharField(max_length = 30)
	position = models.CharField(max_length = 50)		
	firstSupporter = models.CharField(max_length = 60)
	secondSupporter = models.CharField(max_length = 60)
	firstSupportersSupport = models.IntegerField(max_length = 1,default = 0)
	secondSupportersSupport = models.IntegerField(max_length = 1,default = 0)
	eligibility = models.IntegerField(max_length = 1)

#Final list of all the nominee's
class SupportersDetails(models.Model):
	candidatesRollNo = models.CharField(max_length = 10)
	candidatesName =  models.CharField(max_length = 60)
	firstSupporter = models.CharField(max_length = 60)
	secondSupporter = models.CharField(max_length = 60)
	firstSupporterHashKey = models.CharField(max_length = 64)
	secondSupporterHashKey = models.CharField(max_length = 64)


class ListOfNominee(models.Model):
	nomineesName = models.CharField(max_length = 60)
	position = models.CharField(max_length = 50)
	hostel = models.CharField(max_length = 30)
	NumberOfVotes = models.IntegerField(max_length = 7,default = 0)

class VotersList(models.Model):
	voterDetails = models.ForeignKey(UserList)
	goodPassword = models.CharField(max_length = 64)
	evilPassword = models.CharField(max_length = 64)

class Ballot(models.Model):
	voter = models.ForeignKey(VotersList)
	position = models.CharField(max_length = 50)
	nomineeSelected = models.CharField(max_length = 60)
	#this is like a flag
	#if gooPassphrase is used then it is 1 else 0; AS good passphrase can be used only once
	goodPasswordUsed = models.IntegerField(max_length = 1)

class PostsForElection(models.Model):
	hostelsName = models.CharField(max_length = 30)
	position = models.CharField(max_length = 50)

class ListOfSecretary(models.Model):
	hostelsName = models.CharField(max_length = 30)
	position = models.CharField(max_length = 50)
	roolNoOfSecretary = models.CharField(max_length = 10)
	nameOfSecretary = models.CharField(max_length = 50)

