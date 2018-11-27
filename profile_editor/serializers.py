from rest_framework import serializers

from blog.models import Registration, ContactModel


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'registration_title', 'registration_text',)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('id', 'title', 'email', 'message',)
