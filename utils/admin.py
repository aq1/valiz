from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = 'created_at', 'username', 'resolved'
    list_display_links = list_display
    list_filter = 'resolved', 'username'
    ordering = '-created_at', 'username'
    actions = ['resolve']

    def resolve(self, _, queryset):
        queryset.update(resolved=True)
