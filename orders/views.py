from django.shortcuts import render
from rest_framework import views
from .models import Order,OrderDetail
from .serializers import OrderSerializer,OrderDetailSerializer
from backend_ecommerce.helpers import custom_response,parse_request

# Create your views here.
class OrderAPIView(views.APIView):
    def get(self,_):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return custom_response("Get all orders successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all orders failed!', 'Error', None, 400)
    def post(self,request):
        try:
            data = parse_request(request)
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response("Create order successfully!", 'Success', serializer.data, 200)
            return custom_response('Create order failed!', 'Error', serializer.errors, 400)
        except:
             return custom_response('Create order failed!', 'Error', None, 400)

class OrderDetailAPIView(views.APIView):
    def get(self,_):
        try:
            orders = OrderDetail.objects.all()
            serializer = OrderDetailSerializer(orders, many=True)
            return custom_response("Get all order details  successfully!", 'Success', serializer.data, 200)
        except:
            return custom_response('Get all order details failed!', 'Error', None, 400)
    def post(self,request):
        try:
            data = parse_request(request)
            serializer = OrderDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response("Create  order detail successfully!", 'Success', serializer.data, 200)
            return custom_response('Create order detail failed!', 'Error', serializer.errors, 400)
        except:
             return custom_response('Create order detail failed!', 'Error', None, 400)