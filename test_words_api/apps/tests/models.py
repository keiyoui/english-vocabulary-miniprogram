from django.db import models
from django.conf import settings


class TestRecord(models.Model):
    """测试记录模型"""
    TEST_TYPE_CHOICES = [
        ('vocabulary', '词汇量测试'),
        ('speed', '速度测试'),
        ('accuracy', '准确度测试'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    test_type = models.CharField(max_length=20, choices=TEST_TYPE_CHOICES, verbose_name='测试类型')
    difficulty = models.CharField(max_length=20, verbose_name='难度等级')
    total_questions = models.IntegerField(verbose_name='总题目数')
    correct_answers = models.IntegerField(verbose_name='正确答案数')
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='得分')
    vocabulary_level = models.CharField(max_length=20, verbose_name='词汇水平')
    duration = models.IntegerField(verbose_name='测试时长(秒)')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'test_records'
        verbose_name = '测试记录'
        verbose_name_plural = '测试记录'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.nickname} - {self.test_type} - {self.score}"


class Question(models.Model):
    """题目模型"""
    QUESTION_TYPE_CHOICES = [
        ('choice', '选择题'),
        ('fill_blank', '填空题'),
        ('matching', '匹配题'),
    ]
    
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, verbose_name='题目类型')
    question_text = models.TextField(verbose_name='题目内容')
    options = models.JSONField(verbose_name='选项')
    correct_answer = models.CharField(max_length=200, verbose_name='正确答案')
    explanation = models.TextField(blank=True, verbose_name='解释')
    difficulty = models.CharField(max_length=20, verbose_name='难度等级')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'questions'
        verbose_name = '题目'
        verbose_name_plural = '题目'

    def __str__(self):
        return f"{self.question_type} - {self.question_text[:50]}" 