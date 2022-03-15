from rest_framework import api_view
from rest_framework.response import Response

@api_view('GET')
def candles_list(request):
    
    return Response('okay')