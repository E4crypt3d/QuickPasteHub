from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Snippet, User
# Register your models here.

admin.site.register(User, UserAdmin)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'language',
                    'token', 'private', 'created_at', 'modified_at']
    list_display_links = ['id', 'author', 'language',
                          'token', 'private', 'created_at', 'modified_at']
    readonly_fields = ['token']
