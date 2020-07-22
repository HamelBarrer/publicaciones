from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image')
    list_display = ('__str__', 'slug', 'create_at')
