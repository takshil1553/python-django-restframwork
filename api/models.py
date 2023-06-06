from django.db import models

# Create your models here.

#creating company Model

class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    Location = models.CharField(max_length=50)
    #about= models.TextField(max_length=500)
    type= models.TextField(max_length=100,choices=(('IT','IT'),
                                                   ('NON IT','NON IT'),
                                                   ('COMPUTER','COMPUTER')
                                                  ))
    added_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

#creating Emoplyee Model

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    about = models.TextField()
    position = models.TextField(max_length=50 ,choices=(('Manager','manager'),
                                                        ('Software developer','sd'),
                                                        ('Project leader','pl')))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
                                                                                            


   
