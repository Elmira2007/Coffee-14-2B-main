from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length =255,
        verbose_name = "Название"
    )
    image = models.ImageField(
        upload_to="news/"
    )
    descriptions = RichTextField(
        verbose_name = "Описание"
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        
        
class Portfolio(models.Model):
    main_description = models.CharField(
        max_length = 500,
        verbose_name = 'Главное описание'
    )
    title1 = models.CharField(
        max_length = 255,
        verbose_name = 'Название 1'
    )
    description1 = models.CharField(
        max_length = 255,
        verbose_name = 'Описание 1'
    )
    title2 = models.CharField(
        max_length = 255,
        verbose_name = 'Название 2'
    )
    description2 = models.CharField(
        max_length = 255,
        verbose_name = 'Описание 2'
    )
    image = models.ImageField(
        upload_to='portfolio_image/',
        verbose_name='Фотография'
    )
    
    def __str__(self):
        return self.main_description
    
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        