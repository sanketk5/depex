from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    verify_email = models.EmailField()
    text = models.CharField(max_length=30)

class userinfo(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    portfolio_site= models.URLField(blank=True)
    pro_pic = models.ImageField(upload_to='profile_pics', blank=True)
