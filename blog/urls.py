from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('About-me', views.IndexView.as_view(), name='index'),
	path('C++', views.CppView.as_view(), name='cpp'),
	path('Python',  views.PythonView.as_view(), name='python'),
	path('Kontakt', views.ContactView.as_view(), name='contact'),
]