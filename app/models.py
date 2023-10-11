from django.db import models

class Post(models.Model):
    """Model definition for Post. """
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    class Meta:
        ordering = ['created']

class Categoria(models.Model):
    """Model definition for Categoria."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']