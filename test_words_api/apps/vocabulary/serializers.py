from rest_framework import serializers
from .models import Vocabulary


class VocabularySerializer(serializers.ModelSerializer):
    """词汇序列化器"""
    
    class Meta:
        model = Vocabulary
        fields = ['id', 'word', 'phonetic', 'translation', 'difficulty', 'part_of_speech', 
                 'example_sentence', 'frequency', 'created_at']
        read_only_fields = ['id', 'created_at']


class VocabularyDetailSerializer(serializers.ModelSerializer):
    """词汇详情序列化器"""
    
    class Meta:
        model = Vocabulary
        fields = '__all__' 