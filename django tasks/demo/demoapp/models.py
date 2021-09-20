from django.db import models
from datetime import date


# Create your models here.
class Request_Info(models.Model):
	reqid=models.AutoField(primary_key=True)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	dob = models.DateField()
	gender = models.CharField(max_length=50)
	nationality = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pincode = models.IntegerField()
	qualification = models.CharField(max_length=100)
	salary = models.IntegerField()
	pan = models.CharField(max_length=10, unique=True)
	reqdate=models.DateField(default=date.today)
	class Meta:
		db_table = "insertdata"




class Response_Info(models.Model):
	resid=models.AutoField(primary_key=True)
	response = models.CharField(max_length=150)
	class Meta:
		db_table="dispalydata"
	
