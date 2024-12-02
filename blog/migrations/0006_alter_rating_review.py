# Generated by Django 4.2.10 on 2024-11-27 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_rating_image_rating_review_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='blog.review'),
        ),
    ]