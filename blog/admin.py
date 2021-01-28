from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "created_by",
        "updated_by",
        "status",
        "created_on",
        "updated_on",
    )
    list_filter = ("status", "category", "created_by")
    search_fields = ["title", "subtitle"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "title",
                        "subtitle",
                        "slug",
                        "content",
                        "category",
                        "image",
                        "status",
                        "keywords",
                    )
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.updated_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
