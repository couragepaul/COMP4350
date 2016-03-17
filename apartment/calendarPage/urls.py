from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^calendar/createEvent', views.createEvent, name='createEvent'),
    url(r'^calendar/viewEvent', views.viewEvent, name='viewEvent'),
    url(r'^calendar/sendEvent', views.sendEvent, name='sendEvent'),
]