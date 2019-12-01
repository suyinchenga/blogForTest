import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=40)
    #thumbnails to MEDIA_ROOT//blog/thumbnails
    thumbnail = models.ImageField(null=True, upload_to="blog/thumbnails")
    shortDescription = models.CharField(max_length=100)
    #Banners to MEDIA_ROOT/blog/banners
    banner = models.ImageField(upload_to="blog/banners")
    description = models.TextField(default='')
    index = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-index']
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
    def url(self, image_path):
        return os.path.join(settings.MEDIA_URL, str(image_path))
    
    def thumbnail_tag(self):
        return mark_safe('<img src="{}" width="250" height="160" />'.format(self.url(self.thumbnail)))
    
    def banner_tag(self):
        return mark_safe('<img src="{}" width="1200" height="600" />'.format(self.url(self.banner)))
    banner_tag.short_description = 'Banner Image'


class Post(models.Model):
    category_id = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    #Banners to MEDIA_ROOT/blog/banners
    banner = models.ImageField(upload_to="blog/banners")
    description = models.TextField(default='')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)
    published_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-published_on']
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    