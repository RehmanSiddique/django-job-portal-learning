from django.contrib import admin
from core.models import Job, Apply

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'create_by')
    list_filter = ('company', 'location')
    search_fields = ('title', 'company', 'location')

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'applied_date')
    list_filter = ('status', 'applied_date')
    search_fields = ('user__username', 'job__title')
    list_editable = ('status',)
    ordering = ('-applied_date',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user', 'job')