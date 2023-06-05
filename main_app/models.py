from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

AGE_GROUP = (
  ('A', '0-3 Months'),
  ('B', '3-6 Months'),
  ('C', '6-12 Months'),
  ('D', '1-3 Years'),
  ('E', '3-7 Years'),
  ('F', '7-13 Years'),
)

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    age_group = models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('books_detail', kwargs={'pk': self.id})


class Child(models.Model):
    name = models.CharField(max_length=100)
    age_group = models.CharField(
        max_length=1,
        choices=AGE_GROUP,
        default=AGE_GROUP[0][0]
    )
    books = models.ManyToManyField(Book)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'child_id': self.id})