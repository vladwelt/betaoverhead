from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    CHOOSE_TYPE = (('P','Professor'),('D','Director'),('S','Student'))
    user      = models.ForeignKey(User, unique=True)
    type_user = models.CharField(max_length=1,choices=CHOOSE_TYPE)
    phone     = models.CharField(max_length=12)
    address   = models.CharField(max_length=100)