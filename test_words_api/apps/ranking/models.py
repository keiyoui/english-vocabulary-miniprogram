from django.db import models
from django.conf import settings


class Ranking(models.Model):
    """排行榜模型"""
    RANKING_TYPE_CHOICES = [
        ('daily', '日榜'),
        ('weekly', '周榜'),
        ('monthly', '月榜'),
        ('all_time', '总榜'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    ranking_type = models.CharField(max_length=20, choices=RANKING_TYPE_CHOICES, verbose_name='排行榜类型')
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='分数')
    vocabulary_level = models.CharField(max_length=20, verbose_name='词汇水平')
    rank_position = models.IntegerField(verbose_name='排名位置')
    test_count = models.IntegerField(default=1, verbose_name='测试次数')
    period_start = models.DateField(verbose_name='统计开始日期')
    period_end = models.DateField(verbose_name='统计结束日期')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'rankings'
        verbose_name = '排行榜'
        verbose_name_plural = '排行榜'
        unique_together = ['user', 'ranking_type', 'period_start']

    def __str__(self):
        return f"{self.user.nickname} - {self.ranking_type} - {self.rank_position}" 