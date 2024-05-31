from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=25,primary_key=True)
    password=models.CharField(max_length=25)

class Note(models.Model):
    author=models.CharField(max_length=25)
    data=models.TextField()