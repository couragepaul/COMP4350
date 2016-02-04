from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.createMessageView.as_view(), name='createMessageView'),
    url(r'^result/$', views.sentMessageView.as_view(), name='sentMessageView'),
    url(r'^send/$', views.sendMessage, name='sendMessage'),
]