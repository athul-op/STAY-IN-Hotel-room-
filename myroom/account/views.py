
from re import T
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Account

from rest_framework import viewsets
from . serializers import UserSerializer,PasswordSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,BasePermission
from rest_framework.decorators import api_view, permission_classes
from . import otp

# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

    # def list(self, request):
    #     queryset = Account.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer=UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     queryset = Account.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)


class CustomAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True



    
class UserViewSet(viewsets.ModelViewSet):
    '''
    Users
    '''

    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes =[AllowAny]

    def perform_create(self, serializer):
        serializer.save()


    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=id):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    


    @action(detail=False, methods=['post'])
    def send_otp(self,request):
        phone = '+91' + request.data['phone']
        print(phone)
        otp.send(phone)
        return Response ({'Message': f'OTP sent successfully to {phone}'})
    

    @action(detail=False, methods=['post'])
    def verify_otp(self,request):
        code = request.data['otp']
        phone = '+91' + request.data['phone']
        if otp.check(phone,code):
            user = Account.objects.filter(mobile=request.data['phone']).first()
            user.is_active = True
            user.save()
            return Response ({'Message': 'Verified'  })

        return Response({'Message': 'Not Verified'})