from rest_framework.response import Response
from .serializer import StudSerializer
from .models import Student
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
import requests

@api_view(http_method_names=['GET', 'POST'])
def stud_view(request):
    if request.method == 'POST':
        serializer = StudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        obj = Student.objects.all()
        serializer = StudSerializer(obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

@api_view(http_method_names=['GET','PUT','PATCH','DELETE'])
def details_api(request,pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudSerializer(obj)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    if request.method=='DELETE':
        obj.delete()
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        serializer = StudSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        serializer = StudSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def get_carts(request):
    resp = requests.get("https://dummyjson.com/carts")
    if resp.status_code == 200:
        carts = resp.json()
        return Response(data=resp.json(), status=200)
    return Response(data={'detail': 'There is an error'}, status=resp.status_code)


