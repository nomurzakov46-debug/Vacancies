from django.db import models
from django.conf import settings



class Company (models.Model):
    owner  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/',blank=True,null=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


