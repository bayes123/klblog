from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','name','post','created_time']

admin.site.register(Comment, CommentAdmin)
