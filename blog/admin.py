from django.contrib import admin
from .models import Registration, ContactModel, AdminModel

# Register your models here.
admin.site.register(Registration)
admin.site.register(ContactModel, AdminModel)
