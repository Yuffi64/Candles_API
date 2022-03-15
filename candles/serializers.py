from rest_framework import serializers
from .models import Fragrant

class FragrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fragrant
        fields = ['id','scent','seasonal_collection','color','gift_quantity','price','wick_count']
        