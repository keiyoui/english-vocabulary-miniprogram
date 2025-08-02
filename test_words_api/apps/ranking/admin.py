from django.contrib import admin
from .models import Ranking


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ['user', 'ranking_type', 'score', 'vocabulary_level', 'rank_position', 'created_at']
    list_filter = ['ranking_type', 'vocabulary_level', 'created_at']
    search_fields = ['user__nickname', 'user__username']
    readonly_fields = ['created_at'] 