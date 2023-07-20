from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    third_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.third_name}'


class Coord(models.Model):
    latitude = models.FloatField(blank=True)
    longtude = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)


class Level(models.Model):
    winter = models.TextField(blank=True)
    summer = models.TextField(blank=True)
    autumn = models.TextField(blank=True)
    spring = models.TextField(blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Pereval_images(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True)
    images = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f'{self.title} {self.date}'


class Pereval_added(models.Model):
    STATUS = [
        ('new', 'новый'),
        ('pending', 'на рассмотрении'),
        ('accepted', 'успешно'),
        ('rejected', 'не принята')
    ]
    beutytitle = models.TextField(blank=True)
    title = models.TextField(blank=True)
    other_titles = models.TextField(blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.TextField(max_length=10, choices=STATUS, default='new')
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ForeignKey(Pereval_images, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    coord = models.ForeignKey(Coord, on_delete=models.CASCADE)
