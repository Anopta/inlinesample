from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)


class Edition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=256)
    year = models.IntegerField()
    pages = models.IntegerField()


class Testimonial(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    testimonial = models.TextField()
