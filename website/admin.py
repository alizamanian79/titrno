from django.contrib import admin
from .models import Category, Tag, New,Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'journalist', 'newstype', 'active', 'created_at', 'updated_at')
    list_filter = ('newstype', 'active', 'created_at')
    search_fields = ('title', 'description', 'journalist__username')
    prepopulated_fields = {'slug': ('title',)}  
    filter_horizontal = ('categories', 'tags')  


class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email', 'active', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Contact, ContactAdmin)