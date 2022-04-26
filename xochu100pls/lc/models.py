from django.db import models

class Lc(models.Model):
    login = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    status = models.TextField(blank=True)
    education = models.TextField(blank=True)
    foodpreferences = models.TextField(blank=True)
    attitudetoalcohol = models.TextField(blank=True)
    attitudetosmoking = models.TextField(blank=True)

class FriendList(models.Model):
    login1 = models.CharField(max_length=255)
    login2 = models.CharField(max_length=255)

class FriendRequestList(models.Model):
    loginfrom = models.CharField(max_length=255)
    loginto = models.CharField(max_length=255)