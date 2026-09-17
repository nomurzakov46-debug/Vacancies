from django.db import models
from django.contrib.auth.models import User






         
class Profile(models.Model):
    ROLE_CHOICES = (
        ('employer', 'Работодатель'),
        ('candidate', 'Соискатель'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    user = models.OneToOneField(

     User,on_delete=models.CASCADE

    )
class Resume(models.Model):
       title = models.CharField(max_length=250)
       description = models.TextField()
       experience_year = models.IntegerField()
       user = models.ForeignKey(User,on_delete=models.CASCADE)
    



