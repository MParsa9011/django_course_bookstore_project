from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

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
    pages = models.IntegerField(blank=True, null=True   )
    price = models.IntegerField()
    cover = models.ImageField(upload_to="covers/")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='new', blank=True)
    datetime_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommended = models.BooleanField(default=False)
    is_calming = models.BooleanField(default=False)
    is_motivational = models.BooleanField(default=False)
    is_uplifting = models.BooleanField(default=False)
    is_educational = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
