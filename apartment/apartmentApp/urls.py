from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createMessageView', views.createMessageView, name='createMessageView'),
    url(r'^sentMessageView', views.sentMessageView, name='sentMessageView'),
    url(r'^sendMessage', views.sendMessage, name='sendMessage'),
    url(r'^errorMessage', views.errorMessage, name='errorMessage'),
	url(r'^loggedin', views.loggedin, name='loggedin'),
    url(r'^home', views.home, name='home'),
	url(r'^invalidLogin', views.invalidLogin, name='invalidLogin'),
	url(r'^logoutUser', views.logoutUser, name='logoutUser'),
    url(r'^createUser', views.createUser, name='createUser'),
	url(r'^deleteUser', views.deleteUser, name='deleteUser'),
    url(r'^bulletinBoard/$', views.bulletinBoard, name='bulletinBoard'),
    url(r'^bulletinBoard/(?P<bulletin_id>[0-9]+)', views.bulletin, name='bulletin'),
    url(r'^(\w+)/$', views.userMessages.as_view(), name='userMessages'),
    url(r'^(\w+)/(?P<message_id>[0-9]+)/markAsRead', views.markAsRead, name='markAsRead'),
]