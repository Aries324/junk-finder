from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

class ItemsPost(models.Model):
    FURNITURE = ' Furniture'
    ELECTRONICS = 'Electronics'
    HOME_IMPROVEMENT = 'Home Improvement'
    SCRAPS = 'Scraps'
    CLOTHING = 'Clothing'

    ITEM_CHOICES = [
        (FURNITURE, 'Furniture'),
        (ELECTRONICS, 'Electronics'),
        (HOME_IMPROVEMENT, 'Home_Improvement'),
        (SCRAPS, 'Scraps'),
        (CLOTHING, 'Clothing')

    ]
    claimed = models.BooleanField(default=False)
    description = models.TextField()
    title = models.CharField(max_length=200)
    email = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    address = models.URLField()
    items = models.CharField(max_length=20, choices=ITEM_CHOICES)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title