from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializer, ContactSerializer
from blog.models import Registration, ContactModel


class RegistrationViewSet(ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (IsAuthenticated,)


class ContactViewSet(ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
