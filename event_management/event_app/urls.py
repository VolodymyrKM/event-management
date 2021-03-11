from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event_app.views import EventViewSet, EventTypeViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('event', EventViewSet)
router.register('eventtype', EventTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
