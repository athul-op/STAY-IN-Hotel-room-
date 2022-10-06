from django.shortcuts import render

# Create your views here.
from .models import Review
from rest_framework import viewsets
from .serializers import ReviewSerilizer
from rest_framework.permissions import IsAuthenticated


class ReviewViewSet(viewsets.ModelViewSet):
    """
    review
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerilizer
    permission_classes =[IsAuthenticated]

