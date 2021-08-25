from django.db import models

# Create your models here.
class Subsribe(models.Model):

    fname = models.CharField('Имя', max_length=20)
    lname = models.CharField('Фамилия', max_length=20)
    email = models.EmailField('Почта')

    class Meta:
        verbose_name = 'Подпищик'
        verbose_name_plural = 'Подпищики'

    def __str__(self):
        return self.email

class Admission(models.Model):

    fname = models.CharField('Имя', max_length=20)
    lname = models.CharField('Фамилия', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Допуск'
        verbose_name_plural = 'Допуски'

    def __str__(self):
        return self.email

class Blog(models.Model):

    image = models.ImageField(upload_to='static/img')
    text = models.TextField()

class News(models.Model):

    image = models.ImageField(upload_to='static/img/news')
    title = models.CharField(max_length=50)
    badge = models.CharField(max_length=20)

class Courses(models.Model):

    image = models.ImageField(upload_to='static/program')
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

class New(models.Model):
    pass