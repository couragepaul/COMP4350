from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bulletinBoard/$', views.bulletinBoard, name='bulletinBoard'),
    url(r'^bulletinBoard/createBulletin', views.createBulletin, name='createBulletin'),
    url(r'^bulletinBoard/(?P<bulletin_id>[0-9]+)', views.bulletin, name='bulletin'),
    url(r'^bulletinBoard/sendBulletin', views.sendBulletin, name='sendBulletin'),
    url(r'^bulletinBoard/sendComment', views.sendComment, name='sendComment'),
]