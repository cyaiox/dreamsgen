from django.db import models
from django.contrib.auth.models import User
from audio.models import Audio


# Create your models here.
class Group(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Parent')
    name = models.CharField(max_length=64, verbose_name='Name')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')

    def __unicode__(self):
        return '%s' % self.name


class Dream(models.Model):
    group = models.ForeignKey(Group, verbose_name='Category')
    name = models.CharField(max_length=64, verbose_name='Name')
    cover_page = models.FileField(upload_to='cover_pages/', blank=True, verbose_name='Cover Page')
    description = models.CharField(max_length=128, verbose_name='Description')
    introduction = models.TextField(verbose_name='Introduction')
    dream_sound = models.ForeignKey(Audio, related_name='dream_sound', verbose_name='Background Sound')
    alarm_sound = models.ForeignKey(Audio, related_name='alarm_sound', verbose_name='Alarm Sound')
    alarm_time = models.IntegerField(verbose_name='Alarm Time(min)')
    alarm_duration = models.IntegerField(verbose_name='Alarm Duration(sec)')
    alarm_repetition = models.IntegerField(verbose_name='Alarm Repetitions')
    android_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='Android Code')
    ios_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='IOS Code')
    price = models.FloatField(verbose_name='Price')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')

    def __unicode__(self):
        return '%s' % self.name


class Frame(models.Model):
    dream = models.ForeignKey(Dream, verbose_name='Dream', related_name='frames')
    duration = models.IntegerField(verbose_name='Frame Duration(sec)')
    image_source = models.FileField(upload_to='frames/', blank=True, verbose_name='Image Source')
    image_back_source = models.FileField(upload_to='frames/', blank=True, verbose_name='Image Back Source')
    image_repetition = models.IntegerField(verbose_name='Image Repetitions')
    text = models.CharField(max_length=128, verbose_name='Text')
    text_repetition = models.IntegerField(verbose_name='Text Repetitions')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')


class Pack(models.Model):
    dreams = models.ManyToManyField(Dream, blank=True, related_name='packs_dreams', verbose_name='Dreams')
    groups = models.ManyToManyField(Group, blank=True, verbose_name='Categories')
    name = models.CharField(max_length=64, verbose_name='Name')
    description = models.CharField(max_length=128, verbose_name='Description')
    android_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='Android Code')
    ios_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='IOS Code')
    price = models.FloatField(verbose_name='Price')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')

    def __unicode__(self):
        return '%s' % self.description


class Library(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='User')
    dream = models.ForeignKey(Dream, blank=True, null=True, verbose_name='Dream')
    pack = models.ForeignKey(Pack, blank=True, null=True, verbose_name='Pack')
