from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
