from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CandleSerializer
from .models import Candle
from candles import serializers 



@api_view(['GET'])
def candles_list(request):
    candles = Candle.object.all()
    
    serializers = CandleSerializer




# Create your views here.
