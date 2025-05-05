from django.contrib import admin
from .models import Lesson, Category

@admin.register(Lesson)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
