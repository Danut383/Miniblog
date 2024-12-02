from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)  # Agregar imágenes
    rating = models.IntegerField(default=1)  # Calificación de 1 a 5
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Rating(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.review.title} - {self.score}"
