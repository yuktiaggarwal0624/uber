from django.db import models
class Students(models.Model):
    first_name = models.CharField(max_length= 15,null=True,blank=True)
    last_name =models.CharField(max_length= 15,null=True,blank=True)
    birth =models.IntegerField(max_length= 15,null=True,blank=True)
    mobile_number =models.IntegerField(max_length= 15,null=True,blank=True)
    GENDER_TYPES =(
    (1,'Male'),
    (2,'Female'),
    (3,'Other'),
    )
    gender =models.IntegerField(
    choices = GENDER_TYPES,
    
    )
    