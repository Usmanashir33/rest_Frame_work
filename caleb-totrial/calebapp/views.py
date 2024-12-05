from django.shortcuts import render
from .serializers import BookSerialiser
from . models import Book
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
@api_view(["POST","GET"])
def book_list(request ,format=None) :
    
    if request.method == "GET" :
        books = Book.objects.all() # grab all the books
        serializer = BookSerialiser(books,many=True)
        return Response(serializer.data)
        # return JsonResponse({'books':serializer.data})
    
    elif request.method == "POST" : # the sending request
        serialiser = BookSerialiser(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data,status = status.HTTP_201_CREATED)

@api_view(["DELETE","GET","PUT"])        
def book_detail(request ,pk ,format=None):
    try :
        book = Book.objects.get(id = pk)
    except Book.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET" :
        serializer = BookSerialiser(book)
        return Response(serializer.data)
    
    elif request.method == "PUT" :
        serializer = BookSerialiser(book ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE" :
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         
         
         
         