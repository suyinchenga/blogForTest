import os
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

STATUS = (
    (0, "草稿"),
    (1, "发布"),
)


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="标题")
    slug = models.SlugField(max_length=250, null=True, blank=True, verbose_name="别名")
    thumbnail = models.ImageField(null=True, blank=True, upload_to="blog/thumbnails", verbose_name="缩略图")
    shortDescription = models.CharField(max_length=100, verbose_name="简短描述")
    description = models.TextField(default="", verbose_name="描述")
    index = models.IntegerField(default=0, verbose_name="排序值")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="状态")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ["-index"]
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="250" height="160" />'.format(url(self.thumbnail)))
        return "暂无缩略图"

    thumbnail_tag.short_description = "缩略图预览"


class Post(models.Model):
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL, verbose_name="分类")
    title = models.CharField(max_length=250, verbose_name="标题")
    slug = models.SlugField(max_length=250, null=True, blank=True, verbose_name="别名")
    banner = models.ImageField(upload_to="blog/banners", blank=True, verbose_name="封面图")
    description = models.TextField(default="", verbose_name="摘要")
    content = RichTextUploadingField(blank=True, null=True, verbose_name="正文内容")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="状态")
    published_on = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="发布时间")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ["-published_on"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

    def banner_tag(self):
        if self.banner:
            return mark_safe('<img src="{}" width="750" height="300" />'.format(url(self.banner)))
        return "暂无封面图"

    banner_tag.short_description = "封面预览"


class Comment(models.Model):
    post = models.ForeignKey("Post", null=True, on_delete=models.CASCADE, related_name="comments", verbose_name="文章")
    name = models.CharField(max_length=80, verbose_name="昵称")
    email = models.CharField(max_length=250, verbose_name="邮箱")
    text = models.TextField(verbose_name="评论内容")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    approved = models.BooleanField(default=False, verbose_name="已审核")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name="父评论")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return self.name


def url(image_path):
    return os.path.join(settings.MEDIA_URL, str(image_path))
