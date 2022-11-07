from django.contrib import admin

from todo_list_app.models import Tags, Tasks

admin.site.register(Tasks)
admin.site.register(Tags)
