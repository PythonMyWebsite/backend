# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Xác thực người dùng
        user = authenticate(username=username, password=password)
    
        if user:
            # Tạo hoặc cập nhật token cho người dùng
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
def get_user_from_token(token_key):
    try:
        token = Token.objects.get(key=token_key)
        user = token.user
        return user
    except Token.DoesNotExist:
        return None
    
class UserInfoView(APIView):
    def get(self, request):
        # Lấy token từ header của yêu cầu
        token_key = request.headers.get('Authorization')
        print(token_key)
        # Lấy thông tin người dùng từ token
        user = get_user_from_token(token_key)
        
        if user:
            user_info = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            return Response(user_info, status=200)
        else:
            return Response({'error': 'Invalid token'}, status=401)