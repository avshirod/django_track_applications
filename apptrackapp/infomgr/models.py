from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, default=1)
    first_name = models.CharField(max_length=30, default='John')
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, default='Doe')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



class Profile(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, default='abc@def.com')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list

    address = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)

    profile = models.CharField(max_length=50, default='Full Stack Developer')
    skills = models.TextField()
    summary = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.TextField()

    github_link = models.TextField(blank=True)
    linkedin_link = models.TextField(blank=True)
    twitter_link = models.TextField(blank=True)
    portfolio_link = models.TextField(blank=True)