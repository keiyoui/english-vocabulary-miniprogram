from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, UserProfileSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """用户登录"""
    code = request.data.get('code')
    user_info = request.data.get('user_info', {})
    
    if not code:
        return Response({'error': '缺少微信授权码'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 这里应该调用微信API获取openid，暂时模拟
    openid = f"openid_{code}"
    
    # 查找或创建用户
    user, created = User.objects.get_or_create(
        openid=openid,
        defaults={
            'username': openid,
            'nickname': user_info.get('nickName', ''),
            'avatar': user_info.get('avatarUrl', ''),
        }
    )
    
    # 更新用户信息
    if not created:
        user.nickname = user_info.get('nickName', user.nickname)
        user.avatar = user_info.get('avatarUrl', user.avatar)
        user.save()
    
    # 生成JWT token
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'token': str(refresh.access_token),
        'refresh': str(refresh),
        'user': UserSerializer(user).data
    })


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    """获取或更新用户信息"""
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 