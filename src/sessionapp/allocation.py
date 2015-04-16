from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList,RoomList,FriendsPreference
from django.db.models import Max
import random
import math

def sortAllocate(preference):
	roomList = RoomList.objects.all().exclude(counter = 0 ).exclude(counter = -1).order_by('counter')
		
	for room in roomList:
		tosave = RoomList.objects.get(roomNumber = room.roomNumber)
		if room.counter == 1 :
			user = RoomPreference.objects.all().filter(preferedRoom = room.roomNumber , preferenceNumber = preference)
			if user.count() == 1:
				userRoll = user[0].rollNumber
			else :
				userRoll = allocate(room)
		else :
			userRoll = allocate(room)
		setFlags(userRoll , tosave)
		tosave.counter = -1 
		tosave.rollNumber = userRoll
		tosave.save()

def allocate(room):
	V = 0
	candidateId = -1
	candidates = RoomPreference.objects.all().filter(preferedRoom = room.roomNumber, valid = 1)
	
	for eachCandidate in candidates:
		tempV = euclidianV(eachCandidate , room)
		if tempV > V :
			V = tempV
			candidateId = eachCandidate.rollNumber
	if  V != 0 :
		return candidateId
	else :
		return random.choice(candidates).rollNumber

def euclidianV(candidate,room):
	# V = (no of friends / average weighted distance)
	# Weighted distance = distance/weight
	# weight = 6 - pref no
	friendList = FriendsPreference.objects.all().filter(uId = candidate.uId)
	x = room.x
	y = room.y
	tempcount = 0
	for eachFriend in friendList:
		try:
			friendsRoom = RoomList.objects.get(rollNumber = eachFriend.rollNumber)	 		
		except RoomList.DoesNotExist:
			friendsRoom = None
		distance = 0
		if friendsRoom != None:
			# Do not use if not friendsRoom - gives unknown error!
			# Unknown reason, though..
			# Alternative - check if friendsRoom IS None, and then return 0 directly (since tempcount will be zero in any case)
			tempcount += 1
			distance += math.sqrt((friendsRoom.x - x)*(friendsRoom.x - x) + (friendsRoom.y - y)*(friendsRoom.y - y))
			weight = PreferenceTable.objects.get(rollNumber = eachFriend.rollNumber , preferedRoom = friendsRoom.roomNumber)
			distance = distance / (6-weight)

	if tempcount == 0 :
		return 0
	else :
		return tempcount *tempCount /distance

def setFlags(userRoll , room):
	preferenceTableEntries = RoomPreference.objects.all().filter(rollNumber = userRoll)
	for eachEntry in preferenceTableEntries :
		eachEntry.valid = -1
		eachEntry.save()

	preferenceTableEntries2 = RoomPreference.objects.all().filter(preferedRoom = room.roomNumber)
	for eachEntry in preferenceTableEntries2:
		eachEntry.valid = -1
		eachEntry.save()
	
		
	# in preference table , mark all entries of UserID = -1
		# in prefecrence table mark all occurances of room = -1
		# in roomList mark rooms Uid as userID
