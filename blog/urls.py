from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', views.ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
]
