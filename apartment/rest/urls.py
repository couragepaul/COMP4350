from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'messages', views.MessageViewSet, base_name='message')
router.register(r'bulletins', views.BulletinViewSet, base_name='bulletin')
router.register(r'comments', views.CommentViewSet, base_name='comment')

urlpatterns = [
    url(r'^api/', include(router.urls))
]