from django.db import models
from django.contrib.auth.models import User
from dream.models import Dream, Pack
from shoppingcar.models import Plan
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, blank=True, null=True)
    IDENTIFICATION_TYPE = (
        ('P', 'Passport'),
        ('ID', 'Identification'),
        ('D', 'Driver License')
    )
    identification_type = models.CharField(max_length=1, choices=IDENTIFICATION_TYPE, blank=True, null=True)
    identification_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEX, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_mark = models.BooleanField(default=False)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=32)


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    browser_fingerprint = models.CharField(max_length=32)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dream = models.ForeignKey(Dream, blank=True, null=True)
    pack = models.ForeignKey(Pack, blank=True, null=True)


class Experience(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    dream = models.ForeignKey(Dream, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
