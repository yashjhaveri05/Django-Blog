from django.contrib import admin
from .models import Post
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

admin.site.register(Post,PostAdmin)
