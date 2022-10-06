from rest_framework import serializers
from .models import Booked
from .models import Payment


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
       model =Booked
       fields =['count','check_in','check_out','room_id','user_id']


class PaymentSerilizer(serializers.ModelSerializer):
    class Meta:

       model =Payment
       fields =['name','amount','is_paid','created_at','user_id','payment']

