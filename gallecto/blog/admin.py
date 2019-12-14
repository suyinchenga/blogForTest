from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only'
    list_display = ['id', 'title', 'slug', 'status', 'created_on',]
    list_filter = ['status', 'created_on']
    search_fields = ('id', 'title', 'slug')
    list_editable = ['status']
    readonly_fields = ['thumbnail_tag']

class PostAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only'
    list_display = ['id', 'title', 'slug', 'status', 'created_on',]
    list_filter = ['status', 'created_on', 'published_on']
    search_fields = ('id', 'title', 'slug')
    list_editable = ['status']
    readonly_fields = ['banner_tag']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)