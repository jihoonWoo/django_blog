
from django.views.generic.base import TemplateView

#create your view here.

#templateView
class HomeView(TemplateView):
	template_name = 'home.html'