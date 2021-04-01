from django.db import models

class link(models.Model):
    long=models.URLField("URL")
    short=models.CharField(max_length=25)
