from django.shortcuts import render
# Create your views here.
from .models import Books
from .serializers import BookSerializer
from rest_framework import generics


class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# pkを渡す処理側
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
