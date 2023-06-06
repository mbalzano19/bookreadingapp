from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .data import data

AGE_GROUP = (
  ('A', '0-3 Months'),
  ('B', '3-6 Months'),
  ('C', '6-12 Months'),
  ('D', '1-3 Years'),
  ('E', '3-7 Years'),
  ('F', '7-13 Years'),
)


data = data()
print(data[0].get('name'))


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    age_group = models.CharField(
        max_length=1,
        choices=AGE_GROUP,
        default=AGE_GROUP[0][0])
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        AGE_GROUP

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'child_id': self.id})
    
    def __str__(self):
        return f"{self.get_age_group_display()}"
    

