from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min
from django.utils import timezone
from datetime import timedelta
from apps.tests.models import TestRecord


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_statistics(request):
    """获取学习统计"""
    user = request.user
    
    # 基础统计
    total_tests = user.total_tests
    average_score = float(user.average_score)
    vocabulary_level = user.vocabulary_level
    
    # 最近30天的测试记录
    thirty_days_ago = timezone.now() - timedelta(days=30)
    recent_tests = TestRecord.objects.filter(
        user=user,
        created_at__gte=thirty_days_ago
    )
    
    # 按难度统计
    difficulty_stats = recent_tests.values('difficulty').annotate(
        count=Count('id'),
        avg_score=Avg('score'),
        max_score=Max('score'),
        min_score=Min('score')
    )
    
    # 按测试类型统计
    test_type_stats = recent_tests.values('test_type').annotate(
        count=Count('id'),
        avg_score=Avg('score')
    )
    
    # 词汇水平变化
    level_stats = recent_tests.values('vocabulary_level').annotate(
        count=Count('id')
    )
    
    return Response({
        'total_tests': total_tests,
        'average_score': average_score,
        'vocabulary_level': vocabulary_level,
        'difficulty_stats': list(difficulty_stats),
        'test_type_stats': list(test_type_stats),
        'level_stats': list(level_stats),
        'recent_tests_count': recent_tests.count()
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history_statistics(request):
    """获取历史记录统计"""
    test_type = request.GET.get('test_type')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    
    queryset = TestRecord.objects.filter(user=request.user)
    
    if test_type:
        queryset = queryset.filter(test_type=test_type)
    
    if date_from:
        queryset = queryset.filter(created_at__gte=date_from)
    
    if date_to:
        queryset = queryset.filter(created_at__lte=date_to)
    
    # 统计信息
    total_records = queryset.count()
    avg_score = queryset.aggregate(Avg('score'))['score__avg'] or 0
    max_score = queryset.aggregate(Max('score'))['score__max'] or 0
    min_score = queryset.aggregate(Min('score'))['score__min'] or 0
    
    return Response({
        'total_records': total_records,
        'average_score': float(avg_score),
        'max_score': float(max_score),
        'min_score': float(min_score),
        'filter_params': {
            'test_type': test_type,
            'date_from': date_from,
            'date_to': date_to
        }
    }) 