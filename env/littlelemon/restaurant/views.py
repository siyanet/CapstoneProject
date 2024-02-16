from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,Booking 
from . import serializers
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello world!")
def index(request):
    return render(request,'index.html',{})
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]
    
    