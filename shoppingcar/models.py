from django.db import models
from django.contrib.auth.models import User
from dream.models import Group, Dream, Pack


class Coupon(models.Model):
    description = models.CharField(max_length=64, verbose_name='Description')
    percent_discount = models.FloatField(verbose_name='Percent Discount')
    fixed_discount = models.FloatField(verbose_name='Fixed Discount')
    all_products_available = models.BooleanField(default=False, verbose_name='All Products are Available')
    dreams = models.ManyToManyField(Dream, verbose_name='Dreams')
    categories = models.ManyToManyField(Group, verbose_name='Categories')
    packs = models.ManyToManyField(Pack, verbose_name='Packs')
    expiration_date = models.DateTimeField(verbose_name='Available until')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')


class UsedCoupon(models.Model):
    user = models.ForeignKey(User, verbose_name='User')
    coupon = models.ForeignKey(Coupon, verbose_name='Coupon')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Used at')


class PaymentMethod(models.Model):
    description = models.CharField(max_length=64, verbose_name='Description')
    api_key = models.CharField(max_length=128, verbose_name='API Key')
    user_auth = models.CharField(max_length=32, verbose_name='Username Authentication')
    password_auth = models.CharField(max_length=64, verbose_name='Password Authentication')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')


class Price(models.Model):
    added_on = models.DateTimeField(auto_now_add=True, verbose_name='Added on')
    value = models.FloatField(verbose_name='Value')


class Plan(models.Model):
    duration = models.IntegerField(default=30, verbose_name='Duration(day)')
    description = models.CharField(max_length=256, verbose_name='Description')
    price = models.FloatField(verbose_name='Price')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='User')
    dream = models.ForeignKey(Dream, blank=True, null=True, verbose_name='Dream')
    pack = models.ForeignKey(Pack, blank=True, null=True, verbose_name='Pack')
    plan = models.ForeignKey(Plan, blank=True, null=True, verbose_name='Plan')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    price = models.FloatField(verbose_name='Price')
    coupon = models.ForeignKey(Coupon, blank=True, null=True, verbose_name='Coupon Used')
    discount = models.FloatField(blank=True, verbose_name='Discount')
    payment_method = models.ForeignKey(PaymentMethod, blank=True, null=True, verbose_name='Payment Method')