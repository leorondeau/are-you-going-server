from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from areyougoingapi.views import register_user, login_user
from areyougoingapi.views import Events


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'events', Events, 'event')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

