from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from . import plaintext
from .models import Category, Post, Comment

admin.site.site_header = "Gallecto 技术博客管理后台"
admin.site.site_title = "Gallecto 技术博客管理"
admin.site.index_title = "博客管理"


class BaseBlogAdmin(admin.ModelAdmin):
    def id_display(self, obj):
        return obj.id

    id_display.short_description = "编号"


class CategoryAdmin(BaseBlogAdmin):
    list_display = ["id_display", "title", "slug", "status", "created_on"]
    list_filter = ["status", "created_on"]
    search_fields = ["id", "title", "slug"]
    list_editable = ["status"]
    readonly_fields = ["thumbnail_tag", "created_on", "updated_on"]


class PostAdmin(BaseBlogAdmin):
    list_display = ["id_display", "title", "category", "status", "published_on"]
    list_filter = ["status", "created_on", "published_on"]
    search_fields = ["id", "title", "slug"]
    list_editable = ["status"]
    readonly_fields = ["banner_tag", "created_on", "updated_on"]


class CommentAdmin(BaseBlogAdmin):
    list_display = ["id_display", "name", "email", "approved", "created_on"]
    list_filter = ["approved", "created_on"]
    search_fields = ["id", "name", "email"]
    list_editable = ["approved"]
    readonly_fields = ["created_on"]


class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("plaintext_password",)

    def plaintext_password(self, obj):
        return plaintext.get(obj.pk) or "— 未记录（请重置密码）"

    plaintext_password.short_description = "明文密码"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
