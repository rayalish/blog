from django.contrib import admin
from .models import *
# Register your models here.
class CreteAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'publish_date', 'title', 'description', 'author', 'category')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
