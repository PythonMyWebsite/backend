from django.urls import path
from orders import views

urlpatterns = [
    path('order/', views.OrderAPIView.as_view()),
    path('orderdetail/', views.OrderDetailAPIView.as_view()),
]