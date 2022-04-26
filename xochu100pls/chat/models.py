from django.db import models

class Chat(models.Model):
    loginfrom = models.CharField(max_length=255)
    loginto = models.CharField(max_length=255)
    time = models.TimeField(auto_now_add=True)
    message = models.TextField()
