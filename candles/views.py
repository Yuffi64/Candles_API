from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FragrantSerializer 
from .models import Fragrant
from candles import serializers






@api_view(['GET'])
def fragrant_list(request):
    fragrant = Fragrant.objects.all()
    
    serializers = FragrantSerializer(fragrant, many=True)
    
    
    
    
    return Response(serializers.data)