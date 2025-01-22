from django.contrib import admin
from .models import ResumeSubmit

class ResumeSubmitAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'date', 'ip')
    readonly_fields = ('date', 'ip')

# Registra o modelo com a configuração personalizada
admin.site.register(ResumeSubmit, ResumeSubmitAdmin)