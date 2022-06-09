from django.db import models

# Create your models here.

class People(models.Model):
    user_name  = models.CharField(max_length = 1500)
    first_name = models.CharField(max_length = 1500)
    last_name = models.CharField(max_length = 1500)
    email = models.EmailField(max_length = 1500)

    def __str__(self):
        return self.user_name

class Address(models.Model):
    full_name = models.CharField(max_length=1500)
    street_address = models.CharField(max_length = 1500)
    city = models.CharField(max_length = 1500)
    State = models.CharField(max_length = 1500)
    country = models.CharField(max_length = 1500)
    user = models.ForeignKey(People, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length = 1500)
    doctor_contact = models.IntegerField()
    patients_name = models.ManyToManyField(People)
    
    def __str__(self):
        return self.doctor_name

class Product(models.Model):
    product_name = models.CharField(max_length = 1500)
    product_price = models.IntegerField()
    purchased_date =  models.DateField(auto_now_add=True)
    buyers = models.ManyToManyField(People)

    def __str__(self):
        return self.product_name

class Bio(models.Model):
    full_name = models.CharField(max_length=1500)
    bio = models.TextField(max_length = 10000)
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.full_name