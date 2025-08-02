from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'openid', 'vocabulary_level', 'total_tests', 'average_score', 'created_at']
    list_filter = ['vocabulary_level', 'created_at']
    search_fields = ['nickname', 'openid']
    readonly_fields = ['openid', 'created_at', 'updated_at']
    
    fieldsets = (
        ('基本信息', {
            'fields': ('nickname', 'avatar', 'phone')
        }),
        ('学习信息', {
            'fields': ('vocabulary_level', 'total_tests', 'average_score')
        }),
        ('系统信息', {
            'fields': ('openid', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ) 