from rest_framework import serializers
from .models import Book

class BookSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name','description']
        