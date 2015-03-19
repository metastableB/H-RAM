from django.contrib import admin


from sessionapp.models import UserList,FriendsPreference,RoomPreference,StudentBioDataTable,RoomList,AdminDetail
from evoting.models import CandidatesList,ListOfNominee,VotersList,Ballot,PostsForElection,ListOfSecretary,SupportersDetails

     
admin.site.register(UserList)
admin.site.register(FriendsPreference)
admin.site.register(RoomPreference)
admin.site.register(StudentBioDataTable)
admin.site.register(RoomList)

admin.site.register(AdminDetail)
admin.site.register(CandidatesList)
admin.site.register(ListOfNominee)
admin.site.register(VotersList)
admin.site.register(Ballot)
admin.site.register(PostsForElection)
admin.site.register(ListOfSecretary)
admin.site.register(SupportersDetails)

