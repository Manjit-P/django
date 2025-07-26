from django.contrib import admin
from .models import Task
class TodoAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'created_on',
                    'due',
                    )

admin.site.register (Task,TodoAdmin)
