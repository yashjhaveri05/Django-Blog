from django.contrib import admin
from .models import Post,Comment
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {'fields': ["title"]}),
        ("Created By", {'fields': ["author"]}),
        ("Published_Date", {'fields': ["date_posted"]}),
        ("Content", {'fields': ["content"]}),
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('username', 'body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
