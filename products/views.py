from django.http import HttpResponse
from rest_framework import views
from backend_ecommerce.helpers import custom_response,parse_request
from .serializers import CategorySerializer,ProductCommentSerializer,ProductImageSerializer,ProductInfoSerializer,ProductSerializer
from .models import Category,ProductComment,ProductImage,ProductInfo,Product
from rest_framework.parsers import JSONParser
class CategoryAPIView(views.APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            print(categories)
            serializer = CategorySerializer(categories, many=True)
            return custom_response("Get all categories successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all categories failed!', 'Error', None, 400)
        
class CategoryDetailAPIView(views.APIView):
    def get(self, request, id_slug):
        try:
            category = Category.objects.get(id=id_slug)
            serializer = CategorySerializer(category)
            return custom_response("Get category successfully!", 'Success', serializer.data, 200)
        except Category.DoesNotExist:
            return custom_response('Category does not exist!', 'Error', {"message":"id is exist"}, 404)
        except Exception as e:
            return custom_response('Get category failed!', 'Error', str(e), 400)
        
class ProductAPIView(views.APIView):
    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return custom_response("Get all products successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all products failed!', 'Error', None, 400)

class ProductDetailAPIView(views.APIView):
    def get(self, request, id_slug):
        try:
            product = Product.objects.get(id=id_slug)
            serializer = ProductSerializer(product)
            return custom_response("Get product successfully!", 'Success', serializer.data, 200)
        except Product.DoesNotExist:
            return custom_response('Product does not exist!', 'Error', {"message":"id is exist"}, 404)
        except Exception as e:
            return custom_response('Get product failed!', 'Error', str(e), 400)

class ProductImageAPIView(views.APIView):
    def get(self, request,product_id):
        try:
            images = ProductImage.objects.all()
            serializer = ProductImageSerializer(images, many=True)
            return custom_response("Get all images successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all images failed!', 'Error', None, 400)

class ProductCommentAPIView(views.APIView):
    def get(self, request,product_id):
        try:
            comments = ProductComment.objects.get_queryset().filter(product_id=product_id)
            serializer = ProductCommentSerializer(comments, many=True)
            return custom_response("Get all comments successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all comments failed!', 'Error', None, 400)
        
class ProductInfoAPIView(views.APIView):
    def get(self, request,product_id):
        try:
            infos = ProductInfo.objects.get_queryset().filter(product_id=product_id)
            serializer = ProductInfoSerializer(infos, many=True)
            return custom_response("Get all infos successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all infos failed!', 'Error', None, 400)