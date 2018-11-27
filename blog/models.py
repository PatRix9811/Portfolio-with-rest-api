from django.db import models
from django.contrib import admin


# Registration class (wpis)
class Registration(models.Model):
	registration_title = models.CharField(max_length=200)
	registration_text = models.TextField(max_length=5000)
	pub_date = models.DateTimeField('Published date')
	
	def __str__(self):
		return self.registration_title


class ContactModel(models.Model):
	title = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return "{title}: {message}".format(title=self.title, message=self.message)


class AdminModel(admin.ModelAdmin):
	search_fields = ('title', 'email', 'message')
