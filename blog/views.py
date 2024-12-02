from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Review, Rating  # Asegúrate de importar el modelo desde models.py
from django.views import View

# Resto de las vistas aquí...

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'blog/home.html', {'reviews': reviews, 'range': range(1, 6)})

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'blog/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'description', 'genre', 'image', 'rating']  # Ahora incluye la imagen y la calificación
    template_name = 'blog/review_form.html'
    success_url = reverse_lazy('my-reviews')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['title', 'description', 'genre', 'image', 'rating']  # Ahora incluye la imagen y la calificación
    template_name = 'blog/review_form.html'
    success_url = reverse_lazy('my-reviews')


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'blog/review_confirm_delete.html'
    success_url = reverse_lazy('home')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/dashboard.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyReviewsView(LoginRequiredMixin, View):
    def get(self, request):
        reviews = Review.objects.filter(created_by=request.user)
        return render(request, 'blog/my_reviews.html', {'reviews': reviews})
