from django.db import models

# Create your models here.
class Player_info(models.Model):
    number = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    age=models.IntegerField()
    nation=models.CharField(max_length=20)
    team=models.CharField(max_length=30)
    value=models.CharField(max_length=30)

class Image(models.Model):
    author=models.TextField(max_length=100)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',default='')
    text=models.TextField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)