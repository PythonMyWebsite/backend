from . import models
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'image_url',
            'create_at',
            'update_at'
        )

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'price',
            'create_at',
            'update_at',
            'category_id',
            'image_url'  
        )

    def get_image_url(self, obj):
        if obj.thumbnail:
            return obj.thumbnail.url
        return None

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = models.ProductImage
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInfo
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductComment
        fields = '__all__'