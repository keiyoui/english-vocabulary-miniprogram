from django.contrib import admin
from .models import TestRecord, Question


@admin.register(TestRecord)
class TestRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'test_type', 'difficulty', 'score', 'vocabulary_level', 'created_at']
    list_filter = ['test_type', 'difficulty', 'vocabulary_level', 'created_at']
    search_fields = ['user__nickname', 'user__openid']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('基本信息', {
            'fields': ('user', 'test_type', 'difficulty')
        }),
        ('测试结果', {
            'fields': ('total_questions', 'correct_answers', 'score', 'vocabulary_level')
        }),
        ('时间信息', {
            'fields': ('duration', 'start_time', 'end_time', 'created_at')
        }),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_type', 'question_text', 'difficulty', 'is_active', 'created_at']
    list_filter = ['question_type', 'difficulty', 'is_active', 'created_at']
    search_fields = ['question_text', 'correct_answer']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('题目信息', {
            'fields': ('question_type', 'question_text', 'options', 'correct_answer')
        }),
        ('题目设置', {
            'fields': ('difficulty', 'explanation', 'is_active')
        }),
        ('时间信息', {
            'fields': ('created_at',)
        }),
    ) 