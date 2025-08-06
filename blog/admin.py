from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_at')
#     prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Category)
