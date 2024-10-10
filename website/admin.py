# admin.py  

from django.contrib import admin  
from .models import Category, Tag, New  

class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('title',)  
    search_fields = ('title',)  

class TagAdmin(admin.ModelAdmin):  
    list_display = ('title',)  
    search_fields = ('title',)  

class NewAdmin(admin.ModelAdmin):  
    list_display = ('title', 'journalist', 'active', 'created_at', 'updated_at')  
    list_filter = ('active', 'categories', 'tags')  
    search_fields = ('title', 'brief_message', 'description')  
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate slug from title  

admin.site.register(Category, CategoryAdmin)  
admin.site.register(Tag, TagAdmin)  
admin.site.register(New, NewAdmin)