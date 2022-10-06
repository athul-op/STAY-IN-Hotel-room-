from django.shortcuts import render

# Create your views here.
from booking.models import Booked
from .models import Payment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .serializers import BookSerilizer,PaymentSerilizer

class BookedViewSet(viewsets.ModelViewSet):
    """
    booking
    """
    queryset = Booked.objects.all()
    serializer_class = BookSerilizer
    permission_classes =[IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    """
    payment type
    """
    queryset = Payment.objects.all().order_by('id')
    serializer_class = PaymentSerilizer
    permission_classes =[IsAuthenticated]
    