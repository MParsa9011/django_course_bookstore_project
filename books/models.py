from django.db import models
from django.urls import reverse

class Book(models.Model):
    STATUS_CHOICES = (
        ('new', 'نو'),
        ('old', 'دست دوم'),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    translator = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    content = models.TextField()
    pages = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    cover = models.ImageField(upload_to="covers/")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='new', blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])
