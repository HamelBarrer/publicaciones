from django.contrib import admin

from .models import (
    Post,
    Commentary,
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'image')
    list_display = ('__str__', 'slug', 'create_at')


@admin.register(Commentary)
class PostAdmin(admin.ModelAdmin):
    fields = ('commentary',)
    list_display = ('__str__', 'commentary_id', 'user', 'public_date')
