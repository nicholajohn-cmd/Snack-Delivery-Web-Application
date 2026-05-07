from django.db import models

class Food1(models.Model):
    ssnacks  = models.CharField(max_length = 200)
    veg_or_nonveg = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default=False)
    follow_author = models.CharField(max_length=2083, blank=True)  
    book_available = models.BooleanField(default=False)

class Order1(models.Model):
    snacks = models.ForeignKey(Food1, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
    created =  models.DateTimeField(auto_now_add=True) 
class Regis1(models.Model):
    sName = models.CharField(max_length = 200)
    eEmail = models.CharField(max_length = 200)
    sphone = models.CharField(max_length = 12)
    sAddress = models.CharField(max_length = 200)
    sCode = models.CharField(max_length = 200)
    sAgree = models.BooleanField(default=False)
class payments(models.Model):
    s_snacks1  = models.CharField(max_length = 200)
    s_price1 = models.CharField(max_length = 200)
    s_image_url = models.CharField(max_length = 2083, default=False)
    ccardno1=models.CharField(max_length=20)
    Expires=models.CharField(max_length=10)
    CSC=models.CharField(max_length=20)
    F_name=models.CharField(max_length=20)
    Address1=models.CharField(max_length=20) 
    City=models.CharField(max_length=20)
    State1=models.CharField(max_length=20)
    Post_code=models.CharField(max_length=20)
    Mobile_no=models.CharField(max_length=20)
   
    