from dataclasses import Field
from rest_framework import serializers
from .models import Candles

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candles
        Field = ['scent', 'seasonal_collection', 'color','gift_quantity','wick_count','price']
        