# Create your views here
from django.views.generic.base import TemplateView

class Casino(TemplateView):
     template_name = "pages/casino.html"