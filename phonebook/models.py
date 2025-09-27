from django.db import models

# Create your models here.
class Contacts(models.Model):
  name = models.CharField(max_length=150)
  phone_number = models.CharField(max_length=10)
  
  
  
  
class Tasks(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()

class Notes(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()


# migrations files => makemigrations
# hamen ek table banaya 
# 2 fields banaye 