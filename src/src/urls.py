from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','sessionapp.views.validate'),
    url(r'^profilePage/$','sessionapp.views.profile'),
    #url(r'^check/$','sessionapp.views.check'),
    url(r'^login/$','sessionapp.views.login'),
    url(r'^checkSignin/$','sessionapp.views.validate'),
    url(r'^logout/$','sessionapp.views.logout'),
    url(r'^admin/logout/$','sessionapp.views.adminLogout'),
    url(r'^test/$','sessionapp.views.floorPlan'),
    #url(r'^test/$','sessionapp.views.test'),
    url(r'^access/$','sessionapp.views.access'),
    url(r'^bookRoom/$','sessionapp.views.bookRoom'),
    url(r'^floorPlan/$','sessionapp.views.floorPlan'),
    url(r'^openGrid/$','sessionapp.views.openGrid'),
    #url(r'^floor1/$','sessionapp.views.floor1'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','sessionapp.views.home'),

    url(r'^allocate/','sessionapp.views.allocationMethod'),
    url(r'^fpref/','sessionapp.views.friendsprefrence'),
    url(r'^recordFriendsPreference/','sessionapp.views.recordFriendsPreference'),


    #views related to election app
    url(r'^EVoting/$','evoting.views.evotingHomePage'),
    url(r'^EVoting/nominationForm/$','evoting.views.nominationForm1'),
    url(r'^EVoting/nominationForm/(?P<errors>.*)$','evoting.views.nominationForm2'),
    url(r'^EVoting/view/nominees/$','evoting.views.viewNominees'),
    url(r'^EVoting/view/finalResult/$','evoting.views.viewFinalResult'),
    url(r'^EVoting/validateCandidate/$','evoting.views.validateCandidate'),
    url(r'^EVoting/BallotPage/$','evoting.views.BallotPage'),
    url(r'^EVoting/createElectionPasswords/$','evoting.views.createElectionPasswords'),
    url(r'^EVoting/electionPasswordForm/$','evoting.views.electionPasswordForm'),
    url(r'^EVoting/recordVote/$','evoting.views.recordVote'),
    #url(r'^getdetails(.*)/$','evoting.views.getdetails'),

    url(r'^EVoting/charts/$','evoting.views.charts'),
    #These url are only accessed by the administrator
    #url(r'^EVoting/sendmail/$','evoting.views.sendmail'),
    url(r'^EVoting/results/$','evoting.views.finalVoteCount'),
    url(r'^EVoting/admin/$','evoting.views.adminLogin'),
    url(r'^EVoting/admin/home$','evoting.views.adminHomePage'),
    url(r'^EVoting/admin/createFinalNomineesList/$','evoting.views.createFinalNomineesList'),
    url(r'^EVoting/admin/positions-for-election/$','evoting.views.FillElectionPositions'),
    url(r'^EVoting/admin/record-positions-for-election/$','evoting.views.RecordElectionPositions'),
    url(r'^EVoting/verifySupport/(?P<hashedKey>.*)/$','evoting.views.verifySupport'),

    # Dummy links
    #url(r'^webmail$','sessionapp.views.webmail'),
    
)
