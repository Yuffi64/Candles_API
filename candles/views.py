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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
       
             
@api_view(['GET'])
def fragrant_detail(request, pk):
    try:
        fragrant = Fragrant.objects.get(pk=pk)
        serializer = FragrantSerializer(fragrant);
        return Response(serializer.data)
    
    
    
    except Fragrant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);
    
     