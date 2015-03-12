from django.contrib import admin

# Register your models here.
from sessionapp.models import UserList,FriendsPreference,RoomPreference,StudentBioDataTable,RoomList
     
admin.site.register(UserList)
admin.site.register(FriendsPreference)
admin.site.register(RoomPreference)
admin.site.register(StudentBioDataTable)
admin.site.register(RoomList)