from django.db import models
from django.conf import settings
from vacancies.models import Vacancy
from users.models import Resume


class Application(models.Model):
    STATUS_CHOICES = (
        ('new','Новый'),
        ('viewed','Просмотрен'),
        ('accepted','Принят'),
        ('rejected','Отклонен'),
    )
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE,related_name='applications')
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume,on_delete=models.SET_NULL,null=True)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='new')
    created_at = models.DateTimeField(auto_now_add=True)