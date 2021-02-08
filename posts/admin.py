# User admin classes

# Django
from django.contrib import admin
#models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Profile admin

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    search_fields = ('user', 'title')