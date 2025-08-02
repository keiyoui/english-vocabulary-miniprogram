from rest_framework import serializers
from .models import TestRecord, Question


class QuestionSerializer(serializers.ModelSerializer):
    """题目序列化器"""
    
    class Meta:
        model = Question
        fields = ['id', 'question_type', 'question_text', 'options', 'difficulty']


class TestRecordSerializer(serializers.ModelSerializer):
    """测试记录序列化器"""
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = TestRecord
        fields = ['id', 'user', 'user_nickname', 'test_type', 'difficulty', 'total_questions', 
                 'correct_answers', 'score', 'vocabulary_level', 'duration', 'start_time', 
                 'end_time', 'created_at']
        read_only_fields = ['id', 'created_at']


class TestSubmitSerializer(serializers.Serializer):
    """测试提交序列化器"""
    test_id = serializers.CharField()
    answers = serializers.ListField(
        child=serializers.DictField()
    )
    duration = serializers.IntegerField() 