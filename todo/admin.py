from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'end_date', 'is_complete']

admin.site.register(Todo, TodoAdmin)
