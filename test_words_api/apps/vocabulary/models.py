from django.db import models


class Vocabulary(models.Model):
    """词汇模型"""
    DIFFICULTY_CHOICES = [
        ('beginner', '初级'),
        ('intermediate', '中级'),
        ('advanced', '高级'),
        ('professional', '专业级'),
    ]
    
    word = models.CharField(max_length=100, unique=True, verbose_name='单词')
    phonetic = models.CharField(max_length=100, blank=True, verbose_name='音标')
    translation = models.TextField(verbose_name='中文释义')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, verbose_name='难度等级')
    part_of_speech = models.CharField(max_length=50, blank=True, verbose_name='词性')
    example_sentence = models.TextField(blank=True, verbose_name='例句')
    frequency = models.IntegerField(default=0, verbose_name='使用频率')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'vocabulary'
        verbose_name = '词汇'
        verbose_name_plural = '词汇'

    def __str__(self):
        return self.word 