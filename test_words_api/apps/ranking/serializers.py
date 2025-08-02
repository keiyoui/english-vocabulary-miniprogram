from rest_framework import serializers
from .models import Ranking


class RankingSerializer(serializers.ModelSerializer):
    """排行榜序列化器"""
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    user_avatar = serializers.CharField(source='user.avatar', read_only=True)
    
    class Meta:
        model = Ranking
        fields = ['id', 'user', 'user_nickname', 'user_avatar', 'ranking_type', 'score', 
                 'vocabulary_level', 'rank_position', 'test_count', 'period_start', 
                 'period_end', 'created_at']
        read_only_fields = ['id', 'created_at'] 