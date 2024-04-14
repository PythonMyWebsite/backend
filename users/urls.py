from django.urls import path
from users import views

urlpatterns = [
    path('user/register/', views.RegisterView.as_view()),
    path('user/login/', views.LoginView.as_view()),
    path('user/info/', views.UserInfoView.as_view()),
]