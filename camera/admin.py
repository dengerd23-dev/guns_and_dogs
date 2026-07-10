from django.contrib import admin
from django.urls import is_valid_path

from .models import *
# Register your models here.
admin.site.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 10
    list_editable = ('name',)
    list_max_show_all = 20
