from django.db import models
from django.conf import settings


class UserStatistics(models.Model):
    """用户统计模型"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    total_study_time = models.IntegerField(default=0, verbose_name='总学习时长(分钟)')
    total_words_learned = models.IntegerField(default=0, verbose_name='已学单词数')
    total_tests_taken = models.IntegerField(default=0, verbose_name='总测试次数')
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='平均分数')
    highest_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='最高分数')
    consecutive_days = models.IntegerField(default=0, verbose_name='连续学习天数')
    last_study_date = models.DateField(null=True, blank=True, verbose_name='最后学习日期')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'user_statistics'
        verbose_name = '用户统计'
        verbose_name_plural = '用户统计'

    def __str__(self):
        return f"{self.user.nickname} - 统计"


class DailyStatistics(models.Model):
    """每日统计模型"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    date = models.DateField(verbose_name='统计日期')
    study_time = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    tests_taken = models.IntegerField(default=0, verbose_name='测试次数')
    words_learned = models.IntegerField(default=0, verbose_name='学习单词数')
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='平均分数')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'daily_statistics'
        verbose_name = '每日统计'
        verbose_name_plural = '每日统计'
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user.nickname} - {self.date}"


class VocabularyProgress(models.Model):
    """词汇学习进度模型"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    vocabulary = models.ForeignKey('vocabulary.Vocabulary', on_delete=models.CASCADE, verbose_name='词汇')
    is_mastered = models.BooleanField(default=False, verbose_name='是否掌握')
    review_count = models.IntegerField(default=0, verbose_name='复习次数')
    last_review_date = models.DateTimeField(null=True, blank=True, verbose_name='最后复习时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'vocabulary_progress'
        verbose_name = '词汇进度'
        verbose_name_plural = '词汇进度'
        unique_together = ['user', 'vocabulary']

    def __str__(self):
        return f"{self.user.nickname} - {self.vocabulary.word}" 