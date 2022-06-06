from django.db import models

# Create your models here.

class doctor(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField()
    dc_id = models.IntegerField(max_length=60)
    department = models.CharField(max_length=225)
    phone_number = models.IntegerField()

    
