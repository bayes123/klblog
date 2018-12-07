from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.site_header = 'KK博客后台管理'
admin.site.site_title = 'KK的博客'