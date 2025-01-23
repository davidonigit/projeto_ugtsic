from django.contrib import admin
from .models import ResumeSubmit

class ResumeSubmitAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'date', 'ip')
    readonly_fields = ('date', 'ip')

admin.site.register(ResumeSubmit, ResumeSubmitAdmin)