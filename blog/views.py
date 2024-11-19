from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Review
from django.views.generic import DetailView

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'content', 'genre', 'image']
    template_name = 'blog/form.html'

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'content', 'genre', 'image']
    template_name = 'blog/form.html'

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('home')
    template_name = 'blog/confirm_delete.html'

class HomeView(ListView):
    model = Review
    template_name = 'blog/home.html'
    context_object_name = 'reviews'  # Aquí cerramos correctamente

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'blog/detail.html'
    context_object_name = 'review'