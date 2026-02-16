from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'recruiter', 'created_at')
    list_filter = ('created_at', 'location', 'company')
    search_fields = ('title', 'company', 'description')
    readonly_fields = ('created_at', 'updated_at')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'applied_date')
    list_filter = ('status', 'applied_date', 'job')
    search_fields = ('user__username', 'user__email', 'job__title')
    readonly_fields = ('applied_date',)


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
