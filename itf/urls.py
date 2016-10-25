from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='administration'),
    url(r'', include('taekwondo.urls')),
]
