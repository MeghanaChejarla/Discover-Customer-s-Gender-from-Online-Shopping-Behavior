from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)

class gender_prediction(models.Model):

    date_time= models.CharField(max_length=300)
    event_name= models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    product_id= models.CharField(max_length=300)
    category_id= models.CharField(max_length=300)
    category_name= models.CharField(max_length=300)
    brand= models.CharField(max_length=300)
    price= models.CharField(max_length=300)
    user_id= models.CharField(max_length=300)
    session= models.CharField(max_length=300)
    category_1= models.CharField(max_length=300)
    category_2= models.CharField(max_length=300)
    category_3= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



