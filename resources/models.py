from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resource(models.Model):
    user    = models.ForeignKey(User, unique=True)

class Note(models.Model):
    resource = models.ForeignKey(Resource,unique=True)
    note = models.TextField()

class Comment(models.Model):
    resource = models.ForeignKey(Resource,unique=True)
    comment  = models.TextField()
    
class Tag(models.Model):
    resource = models.ManyToManyField(Resource)
    label    = models.TextField()
    