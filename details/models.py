from django.db import models

# Create your models here.

class Bank_Detail(models.Model):
	ifsc=models.CharField(max_length=1000)
	bank_id=models.CharField(max_length=1000)
	branch=models.CharField(max_length=1000)
	address=models.CharField(max_length=1000)
	city=models.CharField(max_length=1000)
	district=models.CharField(max_length=1000)
	state=models.CharField(max_length=1000)
	bank_name=models.CharField(max_length=1000)

	def __str__(self):
		return str(self.bank_name)
