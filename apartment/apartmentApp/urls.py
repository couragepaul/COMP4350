from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^loggedin', views.loggedin, name='loggedin'),
    url(r'^home', views.home, name='home'),
    url(r'^invalidLogin', views.invalidLogin, name='invalidLogin'),
    url(r'^logoutUser', views.logoutUser, name='logoutUser'),
    url(r'^managerSettings', views.managerSettings, name='managerSettings'),
    url(r'^createUser', views.createUser, name='createUser'),
    url(r'^deleteUser', views.deleteUser, name='deleteUser')
]