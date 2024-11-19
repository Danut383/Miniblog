from django.views.generic import ListView
from .models import Review

class HomeView(ListView):
    model = Review
    template_name = 'blog/home.html'
    context_object_name = 'reviews'
