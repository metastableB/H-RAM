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
)
