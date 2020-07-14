from django.db import models

from django.contrib.auth.models import AbstractUser



# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

class ItemsPost(models.Model):
    FURNITURE = ' F'
    ELECTRONICS = 'E'
    HOME_IMPROVEMENT = 'H'
    SCRAPS = 'S'
    CLOTHING = 'C'

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
