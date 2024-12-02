# Generated by Django 4.2.10 on 2024-11-27 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_rating_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='blog.review'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(max_length=50),
        ),
    ]