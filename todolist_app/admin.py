from django.contrib import admin
from todolist_app.models import TaskList  #you can also used .models instead

# Register your models here.

admin.site.register(TaskList)