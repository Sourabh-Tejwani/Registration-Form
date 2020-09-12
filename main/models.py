from django.db import models

# Create your models here.

class User(models.Model):
	first_name=models.CharField(max_length=35)
	last_name=models.CharField(max_length=35)
	email=models.EmailField()
	date_of_birth=models.DateField()
	contact=models.IntegerField()
	gender=models.CharField(max_length=6)
	address=models.CharField(max_length=200)
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	country=models.CharField(max_length=100)

	def __str__(self):
		return self.first_name+" "+self.last_name