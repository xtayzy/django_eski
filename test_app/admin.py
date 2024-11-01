from django.contrib import admin

from test_app.models import Comment, Post, Category

# Register your models here.

admin.site.register([Category, Post, Comment])