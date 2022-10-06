from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .models import Room
from rest_framework import viewsets
from .serializers import VendorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

class VendorPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 500



class VendorViewSet(viewsets.ModelViewSet):
    """
    vendor
    """
    queryset = Room.objects.all()
    serializer_class = VendorSerializer
    permission_classes =[IsAuthenticated]
    pagination_class = VendorPagination

   
