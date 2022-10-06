
from rest_framework import serializers
from .models import Review

class ReviewSerilizer(serializers.ModelSerializer):
    class Meta:

       model =Review
       fields =['feedback','room_id','rating','user_id']