from django.forms import ModelForm
from .models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ('title', 'email', 'message',)
