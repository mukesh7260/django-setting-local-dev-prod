from django.contrib import admin
from .models import * 
# Register your models here.

@admin.register(Mouse) 
class MouseAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','date']   