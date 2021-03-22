from django.db import models


# Create your models here.

class UserProfile(models.Model):

    def tpdefault():
        return 'tpglobalfx'

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    affilliatecode = models.CharField(max_length=200, default=tpdefault)
    passcode=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname + " " + self.lastname
