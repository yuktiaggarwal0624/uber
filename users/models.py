from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length= 15,null=True,blank=True)
    last_name =models.CharField(max_length= 15,null=True,blank=True)
    birth =models.IntegerField(null=True,blank=True)
    mobile_number =models.IntegerField(null=True,blank=True)
    GENDER_TYPES =(
    (1,'Male'),
    (2,'Female'),
    (3,'Other'),
    )
    gender =models.IntegerField(
    choices = GENDER_TYPES,
    
    )
    def __str__(self):
        return str(self.first_name)


class Orders(models.Model):
    
    order_name = models.CharField( max_length=18 , null=True , blank=True)
    order_price = models.IntegerField(null=True , blank=True)
    order_discount = models.IntegerField(null=True , blank=True)
    order_quantity = models.IntegerField(null=True , blank=True)
    order_address = models.TextField( max_length = 18 , null=True , blank=True)
    order_at = models.DateField(null=True , blank=True)


class StudentsAddress(models.Model):
    students=models.ForeignKey(Students,on_delete=models.CASCADE, null=True)
    street=models.CharField(max_length=4 , null=True , blank=True)
    house_number=models.IntegerField(null=True ,blank=True)
    city=models.CharField(max_length=18 , null=True , blank=True)
    country=models.CharField(max_length=4 , null=True , blank=True)
    birth=models.IntegerField(null=True ,blank=True)
    pin_code=models.IntegerField( null=True , blank=True)

    def __str__(self):
        return str(self.street)


    
