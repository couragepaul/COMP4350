from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^createMessageView', views.create_message_view, name='createMessageView'),
    url(r'^sentMessageView', views.sent_message_view, name='sentMessageView'),
    url(r'^sendMessage', views.send_message, name='sendMessage'),
    url(r'^errorMessage', views.error_message, name='errorMessage'),
    url(r'^(\w+)/$', views.UserMessages.as_view(), name='userMessages'),
    #url(r'^(\w+)/(?P<message_id>[0-9]+)', views.message, name='message'),
]