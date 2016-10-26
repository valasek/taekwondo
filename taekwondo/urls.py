"""itf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', lambda r: HttpResponseRedirect('taekwondo/')),
    url(r'^$', views.index, name='index'),
    url(r'^member/$', views.member_list, name='member_list'),
    url(r'^member/new/$', views.member_new, name='member_new'),
    url(r'^member/edit/(?P<pk>\d+)/$', views.member_edit, name='member_edit'),
    url(r'^member/delete/$', views.member_delete, name='member_delete'),
    url(r'^competition/$', views.competition_list, name='competition_list'),
    url(r'^team/$', views.team_list, name='team_list'),
    url(r'^user/$', views.user_list, name='user_list'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
