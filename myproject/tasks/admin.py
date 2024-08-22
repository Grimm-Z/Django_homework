from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Subject)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("name", "description")
    search_fields = ("name", "description")

@admin.register(Teacher)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("name","surname","speciality")
    list_filter = ("surname","speciality")
    search_fields = ("surname","speciality")

@admin.register(School_Class)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("letter","grade")
    list_filter = ("letter","grade")
    search_fields = ("letter","grade")

@admin.register(Student)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("name","surname","grade")
    list_filter = ("surname","grade")
    search_fields = ("surname","grade")