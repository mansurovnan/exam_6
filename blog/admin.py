from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "status",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "status",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "author__username",
    )

    ordering = (
        "-created_at",
    )
admin.site.register(Like)


