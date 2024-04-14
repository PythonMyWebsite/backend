from django.urls import path
from products import views

urlpatterns = [
    path('category/', views.CategoryAPIView.as_view()),
    path("category/<slug:id_slug>/", views.CategoryDetailAPIView.as_view()),
    
    path("product/", views.ProductAPIView.as_view()),
    path("product/<slug:id_slug>/", views.ProductDetailAPIView.as_view()),

    path("product/<slug:product_id>/comments/", views.ProductCommentAPIView.as_view()),

    path("product/<slug:product_id>/images/", views.ProductImageAPIView.as_view()),

    path("product/<slug:product_id>/info/", views.ProductInfoAPIView.as_view()),
]