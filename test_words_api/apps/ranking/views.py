from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Ranking
from .serializers import RankingSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ranking(request):
    """获取排行榜"""
    ranking_type = request.GET.get('ranking_type', 'weekly')
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 50))
    
    # 计算时间范围
    today = timezone.now().date()
    if ranking_type == 'daily':
        period_start = today
        period_end = today
    elif ranking_type == 'weekly':
        period_start = today - timedelta(days=today.weekday())
        period_end = period_start + timedelta(days=6)
    elif ranking_type == 'monthly':
        period_start = today.replace(day=1)
        if today.month == 12:
            period_end = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            period_end = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
    else:  # all_time
        period_start = None
        period_end = None
    
    queryset = Ranking.objects.filter(ranking_type=ranking_type)
    
    if period_start and period_end:
        queryset = queryset.filter(period_start=period_start, period_end=period_end)
    
    # 按分数排序
    queryset = queryset.order_by('-score', 'rank_position')
    
    # 分页
    start = (page - 1) * page_size
    end = start + page_size
    ranking_list = queryset[start:end]
    
    serializer = RankingSerializer(ranking_list, many=True)
    
    return Response({
        'rankings': serializer.data,
        'total_count': queryset.count(),
        'page': page,
        'page_size': page_size,
        'ranking_type': ranking_type
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_rank(request):
    """获取用户排名"""
    ranking_type = request.GET.get('ranking_type', 'weekly')
    
    try:
        ranking = Ranking.objects.filter(
            user=request.user,
            ranking_type=ranking_type
        ).order_by('-created_at').first()
        
        if ranking:
            serializer = RankingSerializer(ranking)
            return Response(serializer.data)
        else:
            return Response({'error': '用户未上榜'}, status=status.HTTP_404_NOT_FOUND)
    except Ranking.DoesNotExist:
        return Response({'error': '用户未上榜'}, status=status.HTTP_404_NOT_FOUND)
 