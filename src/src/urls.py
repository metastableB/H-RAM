from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','sessionapp.views.home'),
    url(r'^register/$','sessionapp.views.register'),
    url(r'^check/$','sessionapp.views.check'),
    url(r'^signin/$','sessionapp.views.signin'),
    url(r'^checkSignin/$','sessionapp.views.check_signin'),
    url(r'^admin/', include(admin.site.urls)),
)
