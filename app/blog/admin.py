from django.contrib import admin

# Register your models here.
from .models import Article, Comment

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
# pass

admin.site.register(Article)
admin.site.register(Comment)
