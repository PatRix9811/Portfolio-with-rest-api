from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegistrationViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'registration', RegistrationViewSet)
router.register(r'contact', ContactViewSet)

app_name = 'profile_editor'
urlpatterns = [
    path('', include(router.urls)),
]
