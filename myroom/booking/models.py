from django.db import models
from vendor.models import Room
from account.models import Account

# Create your models here.
class Booked(models.Model):
    room_id =models.ForeignKey(Room,on_delete=models.CASCADE)
    count = models.IntegerField()
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE)





class Payment(models.Model):
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE) 
    name =models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment= models.ForeignKey(Booked,on_delete=models.CASCADE) 
    # razorpay_payment_id= models.CharField(max_length=100, blank=True,null=True)  
    # payment_method=models.CharField(max_length=100)
    is_paid =models.BooleanField(default=False)
#     created_at=models.DateField(auto_now_add=True)    