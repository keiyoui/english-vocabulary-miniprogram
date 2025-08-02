from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """用户模型"""
    openid = models.CharField(max_length=100, unique=True, verbose_name='微信OpenID')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    avatar = models.URLField(max_length=500, blank=True, verbose_name='头像')
    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    vocabulary_level = models.CharField(max_length=20, default='beginner', verbose_name='词汇水平')
    total_tests = models.IntegerField(default=0, verbose_name='总测试次数')
    average_score = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='平均分数')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.nickname or self.username 