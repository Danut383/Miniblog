from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
