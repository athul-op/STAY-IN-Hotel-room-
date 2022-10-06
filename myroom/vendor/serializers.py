from rest_framework import serializers
from .models import Account
from .models import Room


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['is_verified','has_ac','price','description','is_available','vendor_id','image','service','city','district','pin','street']
        


    # def create(self, validated_data):

    #     user = Account(
    #         # email=validated_data['email'],
    #         is_vendor=validated_data['is_vendor'],
    #         # number=validated_data['number']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
