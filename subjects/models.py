from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource

class Content(models.Model):
    title     = models.TextField(max_length=100)
    content   = models.TextField()
    reference = models.TextField(max_length=300)
    comment   = models.TextField(max_length=200)

class Subject(models.Model):
    CHOOSE_VISIBILITY = (('P','Public'),('L','Limited'))
    code        = models.BigIntegerField()
    label       = models.TextField(max_length=60)
    description = models.TextField()
    visibility  = models.CharField(max_length=1,choices=CHOOSE_VISIBILITY)
    user        = models.ForeignKey(User,unique=True)
    resurce     = models.ManyToManyField(Resource)
    content     = models.ManyToManyField(Content)

    