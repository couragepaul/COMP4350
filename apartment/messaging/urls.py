from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^messageView', views.message_view, name='messageView'),
    url(r'^sentMessageView', views.sent_message_view, name='sentMessageView'),
    url(r'^sendMessage', views.send_message, name='sendMessage'),
    url(r'^errorMessage', views.error_message, name='errorMessage'),
    url(r'^message', views.message, name='message'),
]