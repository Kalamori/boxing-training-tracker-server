from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=254)
    bio = models.TextField(max_length=300, default="Jab, Cross, Hook, Uppercrust!")

    def __str__(self):
        return self.username
    