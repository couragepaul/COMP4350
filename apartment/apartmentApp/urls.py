from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createMessageView', views.createMessageView, name='createMessageView'),
    url(r'^sentMessageView', views.sentMessageView, name='sentMessageView'),
    url(r'^sendMessage', views.sendMessage, name='sendMessage'),
    url(r'^errorMessage', views.errorMessage, name='errorMessage'),
]