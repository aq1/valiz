from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = 'created_at', 'username', 'resolved'
    readonly_fields = ['created_at']
    list_display_links = list_display
    list_filter = 'resolved', 'username'
    ordering = '-created_at', 'username'
    actions = ['resolve']

    def get_queryset(self, request):
        return super(LogAdmin, self).get_queryset(request).filter(resolved=False)

    def resolve(self, _, queryset):
        queryset.update(resolved=True)
