from django.db import models


class TLogin(models.Model):
    username = models.CharField(max_length=10)
    passcode = models.CharField(max_length=10)
