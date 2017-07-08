from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')

    def __unicode__(self):
        return '%s' % self.name


class Audio(models.Model):
    category = models.ForeignKey(Group, verbose_name='Category')
    description = models.CharField(max_length=128, verbose_name='Description')
    source = models.FileField(upload_to='audios/', blank=True, verbose_name='File')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')

    def __unicode__(self):
        return '%s' % self.description

