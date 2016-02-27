from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bulletinBoard/$', views.bulletinBoard, name='bulletinBoard'),
    url(r'^bulletinBoard/createBulletin', views.createBulletin, name='createBulletin'),
    url(r'^bulletinBoard/viewBulletin', views.viewBulletin, name='viewBulletin'),
    url(r'^bulletinBoard/sendBulletin', views.sendBulletin, name='sendBulletin'),
    url(r'^bulletinBoard/sendComment', views.sendComment, name='sendComment'),
]