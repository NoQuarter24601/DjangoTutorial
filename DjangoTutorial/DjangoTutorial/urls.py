"""
Definition of urls for DjangoTutorial.
"""

from django.conf.urls import include, url
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),

    # Examples:
    # url(r'^$', DjangoTutorial.views.home, name='home'),
    # url(r'^DjangoTutorial/', include('DjangoTutorial.DjangoTutorial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
]
