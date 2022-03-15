from dataclasses import Field
from rest_framework import serializers
from .models import Candle

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candle
        Field = ['scent', 'seasonal_collection', 'color','gift_quantity','wick_count','price']
        