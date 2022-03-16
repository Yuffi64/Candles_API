from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FragrantSerializer 
from .models import Fragrant





@api_view(['GET', 'POST'])
def fragrant_list(request):
    
    if request.method == 'GET':
        fragrant = Fragrant.objects.all()
        serializers = FragrantSerializer(fragrant, many=True) 
        return Response(serializers.data)
    
    
    
    elif request.method == 'POST':
        serializer = FragrantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
       
       
             
@api_view(['GET', 'PUT','DELETE'])
def fragrant_detail(request, pk):
    fragrant = get_object_or_404(Fragrant, pk=pk)
    if request.method == 'GET':
        serializer = FragrantSerializer(fragrant);
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = FragrantSerializer(fragrant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        fragrant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
