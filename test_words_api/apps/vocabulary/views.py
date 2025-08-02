from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Vocabulary
from .serializers import VocabularySerializer, VocabularyDetailSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vocabulary_list(request):
    """获取词汇列表"""
    difficulty = request.GET.get('difficulty')
    search = request.GET.get('search')
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 20))
    
    queryset = Vocabulary.objects.filter(is_active=True)
    
    if difficulty:
        queryset = queryset.filter(difficulty=difficulty)
    
    if search:
        queryset = queryset.filter(
            Q(word__icontains=search) | 
            Q(translation__icontains=search)
        )
    
    # 分页
    start = (page - 1) * page_size
    end = start + page_size
    vocabulary_list = queryset[start:end]
    
    serializer = VocabularySerializer(vocabulary_list, many=True)
    
    return Response({
        'results': serializer.data,
        'total_count': queryset.count(),
        'page': page,
        'page_size': page_size
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vocabulary_detail(request, word):
    """获取词汇详情"""
    try:
        vocabulary = Vocabulary.objects.get(word=word, is_active=True)
        serializer = VocabularyDetailSerializer(vocabulary)
        return Response(serializer.data)
    except Vocabulary.DoesNotExist:
        return Response({'error': '词汇不存在'}, status=status.HTTP_404_NOT_FOUND) 