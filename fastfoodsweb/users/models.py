from django.db import models
from django.contrib.auth.models import User

from cart.models import Address

class Profile(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=50)
    phonenum = models.CharField(max_length=10,blank=True,null=True,default=None)
    def __str__(self):
        return self.customer.username
    class Meta:
        verbose_name_plural = 'Thông tin người dùng'
        
    
    