from django.db import models
from account.models import Account
from vendor.models import Room
# Create your models here.

class Review(models.Model):
    # review = models.TextField(null=True,blank=True)
    rating = models.IntegerField()
    feedback = models.TextField(null=True,blank=True)
    user_id = models.ForeignKey(Account,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)