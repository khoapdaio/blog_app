from django.contrib import admin

from Blog.models import Author, Tag, Category, Post


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)


class AuthorAdmin(admin.ModelAdmin):
	list_display = ("username", "email")


class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "category", "published", "publish_date", "date_created")


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
