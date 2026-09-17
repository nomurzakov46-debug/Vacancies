from django.db import models
from companies.models import Company
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Vacancy(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='vacancies',null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_from = models.IntegerField(null=True,blank=True)
    salary_to = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"