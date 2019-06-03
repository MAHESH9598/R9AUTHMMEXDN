from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pid','pname','pcost','pmfdt','pexpdt')