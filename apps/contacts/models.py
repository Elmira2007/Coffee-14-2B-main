from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    email = models.EmailField(
        verbose_name = "Возраст пользователя"
    )
    subject = models.CharField(
        max_length = 255,
        verbose_name = "Вопроc пользователя"
    )
    massage = models.TextField(
        verbose_name = "Cообщения пользователя"
    )
    
        
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        