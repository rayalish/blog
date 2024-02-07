from django.contrib import admin
from .models import *
# Register your models here.
class CreateAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'publish_date', 'title', 'description', 'author', 'category')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
admin.site.register(Blog, CreateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
