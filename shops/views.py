from django.views.generic import ListView, DetailView
from .models import Shop

class Home(ListView):
    model = Shop
    template_name = "home.html"

home = Home.as_view()

class Detail(DetailView):
    model = Shop
    template_name = "shops/detail.html"

detail = Detail.as_view()
