from rest_framework import serializers
from .models import UserStatistics, DailyStatistics, VocabularyProgress


class UserStatisticsSerializer(serializers.ModelSerializer):
    """用户统计序列化器"""
    
    class Meta:
        model = UserStatistics
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class DailyStatisticsSerializer(serializers.ModelSerializer):
    """每日统计序列化器"""
    
    class Meta:
        model = DailyStatistics
        fields = '__all__'
        read_only_fields = ['id', 'created_at']


class VocabularyProgressSerializer(serializers.ModelSerializer):
    """词汇进度序列化器"""
    vocabulary_word = serializers.CharField(source='vocabulary.word', read_only=True)
    vocabulary_translation = serializers.CharField(source='vocabulary.translation', read_only=True)
    
    class Meta:
        model = VocabularyProgress
        fields = ['id', 'vocabulary', 'vocabulary_word', 'vocabulary_translation', 
                 'is_mastered', 'review_count', 'last_review_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at'] 