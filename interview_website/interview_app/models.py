from django.db import models

# Create your models here.

class Customer(models.Model):
    STATUS = (

        ('Employeed', 'Employeed'),
        ('Looking for Job', 'Looking for Job'),
        ('Doing Internship', 'Doing Internship'),

    )
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10, null=True)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    employment_status= models.CharField(max_length=30, null=True, choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

