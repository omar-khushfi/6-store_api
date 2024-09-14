from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):
    review=serializers.SerializerMethodField(method_name='get_review',read_only=True)
    class Meta:
        model=Product
        fields="__all__"
        
    def get_review(self,obj):
        reviews=obj.reviews.all()
        serializers=ReviewSerializers(reviews,many=True)
        return serializers.data
        
        
        
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
        
        
        
        
