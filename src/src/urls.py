from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','sessionapp.views.validate'),
    url(r'^profilePage/$','sessionapp.views.profile'),
    url(r'^myprofile/$','sessionapp.views.myprofile'),
    url(r'^login/$','sessionapp.views.login'),
    url(r'^checkSignin/$','sessionapp.views.validate'),
    url(r'^logout/$','sessionapp.views.logout'),
    url(r'^admin/logout/$','evoting.views.adminLogout'),
    url(r'^test/$','sessionapp.views.floorPlan'),    url(r'^access/$','sessionapp.views.access'),
    url(r'^bookRoom/$','sessionapp.views.bookRoom'),
    url(r'^floorPlan/$','sessionapp.views.floorPlan'),
    url(r'^messages/$','sessionapp.views.messages'),
    url(r'^openGrid/$','sessionapp.views.openGrid'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','sessionapp.views.home'),

    url(r'^about/','sessionapp.views.about'),
    url(r'^contact/','sessionapp.views.contact'),

    url(r'^changepassword/','sessionapp.views.changepassword'),


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
    url(r'^EVoting/generate_PDF/$','evoting.views.generate_PDF'),
    url(r'^EVoting/nominee/(?P<nomineesRollno>[0-9]{4}[A-Za-z]{2}[0-9]{2,3})/$','evoting.views.aboutNominee'),
    url(r'^EVoting/charts/$','evoting.views.charts'),
    #These url are only accessed by the administrator
    url(r'^EVoting/results/$','evoting.views.finalVoteCount'),
    url(r'^administrator/$','evoting.views.adminLogin'),
    url(r'^administrator/check/$','evoting.views.adminLoginCheck'),
    url(r'^administrator/check_valid_users/$','evoting.views.checkValidUsers'),
    url(r'^administrator/register_users/$','evoting.views.registerUsers'),
    url(r'^administrator/home/$','evoting.views.adminHomePage'),
    url(r'^administrator/createFinalNomineesList/$','evoting.views.createFinalNomineesList'),
    url(r'^administrator/positions-for-election/$','evoting.views.FillElectionPositions'),
    url(r'^administrator/record-positions-for-election/$','evoting.views.RecordElectionPositions'),
    url(r'^EVoting/verifySupport/(?P<hashedKey>.*)/$','evoting.views.verifySupport'),

    # Dummy links
    #url(r'^webmail$','sessionapp.views.webmail'),
    
)
