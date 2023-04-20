from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Popularplace(models.Model):
    img = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    visible = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Popularplace"
        verbose_name_plural = "Popularplace"
    
class Popularplace1(models.Model):
    img = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    visible = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Popularplace1"
        verbose_name_plural = "Popularplace1"

class Booking(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    date = models.DateField()
    totaladults = models.IntegerField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Booking"

class AddReview(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=50)

