from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bulletinBoard/$', views.bulletinBoard, name='bulletinBoard'),
    url(r'^bulletinBoard/createBulletin', views.createBulletin, name='createBulletin'),
    url(r'^bulletinBoard/(?P<bulletin_id>[0-9]+)', views.bulletin, name='bulletin'),
]