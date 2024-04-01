from django.db import models

class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография пользователя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = "Профессия"
    )
    age = models.IntegerField(
        verbose_name = "Возраст"
    )
    froms = models.CharField(
        max_length = 255,
        verbose_name ="Место рождения"
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    locate = models.CharField(
        max_length = 255,
        verbose_name = "Адрес"      
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Телефонный номер"    
    )
    instagram =  models.URLField(
        verbose_name = "Instagram ссылка",
        blank = True,null = True
    )
    facebook =  models.URLField(
        verbose_name = "Facebook ссылка",
        blank = True,null = True
    )
    youtube =  models.URLField(
        verbose_name = "Youtube ссылка",
        blank = True,null = True
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"
        

class Secondary(models.Model):
    image = models.ImageField(
        upload_to="secondary/",
        verbose_name="Фотография пользователя"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о себе"
    )
    descriptions = models.TextField(
        verbose_name = "О себе"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О пользователе"
        verbose_name_plural = "О пользователей"

class Testim(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография пользователя"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = "Профессия"
    )
    descriptions = models.TextField(
        verbose_name = "Описание"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
