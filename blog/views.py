from .models import Registration
from django.views import generic
from .forms import ContactForm


class IndexView(generic.ListView):
	queryset = Registration.objects.filter(registration_title='About me')
	template_name = 'blog/index.html'
	context_object_name = 'chose_registration'


class CppView(generic.ListView):
	queryset = Registration.objects.filter(registration_title='C++')
	template_name = 'blog/index.html'
	context_object_name = 'chose_registration'

		
class PythonView(generic.ListView):
	queryset = Registration.objects.filter(registration_title='Python')
	template_name = 'blog/index.html'
	context_object_name = 'chose_registration'


class ContactView(generic.FormView):
	template_name = 'blog/form.html'
	form_class = ContactForm
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super(ContactView, self).form_valid(form)



