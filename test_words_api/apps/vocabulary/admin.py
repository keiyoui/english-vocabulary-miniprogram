from django.contrib import admin
from .models import Vocabulary


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ['word', 'phonetic', 'difficulty', 'part_of_speech', 'frequency', 'is_active', 'created_at']
    list_filter = ['difficulty', 'part_of_speech', 'is_active', 'created_at']
    search_fields = ['word', 'translation']
    readonly_fields = ['created_at'] 