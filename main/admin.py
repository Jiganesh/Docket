from django.contrib import admin
from .models import ToDoList, Item

admin.site.register(ToDoList)
admin.site.register(Item)

# Register your models here.
