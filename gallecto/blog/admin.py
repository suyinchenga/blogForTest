from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    readonly_fields = ['thumbnail_tag', 'banner_tag']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)