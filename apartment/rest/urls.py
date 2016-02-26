from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'messages', views.MessageViewSet, base_name='message')

urlpatterns = [
    url(r'^api/', include(router.urls))
]