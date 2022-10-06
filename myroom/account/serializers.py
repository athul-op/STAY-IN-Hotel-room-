from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username','is_active','email','password','mobile','is_vendor']
        extra_kwargs =  {'email':{'write_only':True,'required':True},'password': {'write_only': True},'mobile':{'required':True}}

    def create(self, validated_data):

        user = Account(
            email=validated_data['email'],
            username=validated_data['username'],
            mobile=validated_data['mobile']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =['password']


# class AccountSerializer(serializers.ModelSerializer):

#     # profile         = ProfileSerializer(read_only=True)

#     class Meta:
#         model = Account
#         fields = '__all__'

#         fields = ['id','email','mobile','is_active','password','profile']
#         extra_kwargs={'email':{'required':True},'password': {'write_only': True},'is_active':{'read_only' : True}}

#     def create(self, validated_data):
#         user = Account(
#                 email      = validated_data['email'],
#                 mobile     = validated_data['mobile'],
                
#             )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user        