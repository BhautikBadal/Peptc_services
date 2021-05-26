from django.db import models

# Create your models here.

class service_reg(models.Model):

    s_id = models.AutoField(primary_key=True)
    ser_user_name = models.CharField(max_length=30 , default='NULL22')
    user_name = models.CharField(max_length=30)
    service_name = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

class reg_service_provider(models.Model):

    r_id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)