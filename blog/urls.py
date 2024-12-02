from django.urls import path
from .views import *

urlpatterns = [
    path('', ReviewListView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('my_reviews/', MyReviewsView.as_view(), name='my-reviews'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
