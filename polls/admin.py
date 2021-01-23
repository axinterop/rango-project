from django.contrib import admin
from polls.models import Category, Page


class PageInLine(admin.StackedInline):
    model = Page
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Stats:', {'fields': ['views', 'likes']}),
    ]
    inlines = [PageInLine]

    list_display = ('name', "views", "likes")


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)
