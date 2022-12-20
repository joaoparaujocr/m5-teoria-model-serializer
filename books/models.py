from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    description = models.TextField()