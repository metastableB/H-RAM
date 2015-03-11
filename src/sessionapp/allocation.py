from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.context_processors import csrf
from sessionapp.models import RoomPreference,UserList,RoomList
from django.db.models import Max
import random

def sortAllocate( preference , iThPreferences):
	roomList = RoomList.objects.all().exclude(count = 0 ).exclude(count = -1)
	#roomList = roomList.objects.all().order_by('count')
	
	for room in roomList:
		if room.count == 1 :
			userRoll = RoomPreference.objects.all().filter(preferedRoom = room.roomNumber).rollNumber
		else :
			userRoll = allocate(room)
		setFlags(userRoll , room)
		room.count = -1 

def allocate(room):
	V = -1
	candidateId = -1
	condidates = RoomPreference.objects.all().filter(preferedRoom = room, valid = 1)
	
	for eachCandidate in candidates:
		tempV = eculidianV(eachCandidate , room)
		if tempV > V :
			V = tempV
			candidateId = eachCandidate.rollNumber
	if V!= -1 :
		return candidateId
	else :
		return random.choice(candidates).rollNumber

def euclidianV(candidate,room):
	friendList = FriendsPreference.objects.all().fileter(uId = candidate.uId)
	x = room.x
	y = room.y
	count = 0
	for eachFriend in friendList:
		friendsRoom = RoolList.objects.all().filter(uId = eachFriend.uId)
		if friendsRoom != None:
			count += 1
			distance += math.sqrt((friendsRoom.x - x)*(friendsRoom.x - x) + (friendsRoom.y - y)*(friendsRoom.y - y))

	if count == 0 :
		return 0
	else :
		return distance/count 

def setFlags(userId , room):
	preferenceTableEntries = RoomPreference.objects.all().filter(uId = userId)
	for eachEntry in preferenceTableEntries :
		eachEntry.valid = -1

	preferenceTableEntries2 = RoomPreference.objects.all().filter(preferedRoom = room.roomNumber)
	for eachEntry in preferenceTableEntries2:
		eachEntry.valid = -1
	room.uId = userId	
		
	# in preference table , mark all entries of UserID = -1
		# in prefecrence table mark all occurances of room = -1
		# in roomList mark rooms Uid as userID
