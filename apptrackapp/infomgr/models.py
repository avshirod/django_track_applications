from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# Create your models here.

class UserInfo(models.Model):
    first_name = models.CharField(max_length=30, default='John')
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, default='Doe')

    email = models.EmailField(max_length=50, default='abc@def.com')
    # user = models.OneToOneField(User, on_delete=models.CASCADE) #FName, LName Username, Email, Password

    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list

    address = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)

    summary = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.TextField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserInfo.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.userinfo.save()
