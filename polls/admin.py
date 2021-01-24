from django.contrib import admin
from polls.models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', "views", "likes")
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')


class PageInLine(admin.StackedInline):
    model = Page
    extra = 0


admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)
