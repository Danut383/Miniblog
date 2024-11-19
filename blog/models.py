from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, choices=[
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
    ])
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
