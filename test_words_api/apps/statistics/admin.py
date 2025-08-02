from django.contrib import admin
from .models import UserStatistics, DailyStatistics, VocabularyProgress


@admin.register(UserStatistics)
class UserStatisticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_study_time', 'total_words_learned', 'total_tests_taken', 
                   'average_score', 'highest_score', 'consecutive_days', 'last_study_date']
    list_filter = ['consecutive_days', 'last_study_date', 'created_at']
    search_fields = ['user__nickname', 'user__openid']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(DailyStatistics)
class DailyStatisticsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'study_time', 'tests_taken', 'words_learned', 'average_score']
    list_filter = ['date', 'created_at']
    search_fields = ['user__nickname', 'user__openid']
    readonly_fields = ['created_at']


@admin.register(VocabularyProgress)
class VocabularyProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'vocabulary', 'is_mastered', 'review_count', 'last_review_date']
    list_filter = ['is_mastered', 'last_review_date', 'created_at']
    search_fields = ['user__nickname', 'vocabulary__word']
    readonly_fields = ['created_at', 'updated_at'] 