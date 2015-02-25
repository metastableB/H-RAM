from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','sessionapp.views.home'),
    url(r'^profilePage/$','sessionapp.views.profile'),
    #url(r'^check/$','sessionapp.views.check'),
    url(r'^login/$','sessionapp.views.login'),
    url(r'^checkSignin/$','sessionapp.views.validate'),
    url(r'^logout/$','sessionapp.views.logout'),
    url(r'^test/$','sessionapp.views.test'),
    url(r'^access/$','sessionapp.views.access'),
    url(r'^bookRoom/$','sessionapp.views.bookRoom'),
    url(r'^admin/', include(admin.site.urls)),
)
