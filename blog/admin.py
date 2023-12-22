from django.contrib import admin
from blog.models import Tag, Category, Page


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',

    # preenche o slug automático no django admin
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',

    # preenche o slug automático no django admin
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'full_name', 'is_published',
    list_display_links = 'full_name',
    search_fields = 'id', 'slug', 'full_name', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',

    # preenche o slug automático no django admin
    prepopulated_fields = {
        'slug': ('full_name',),
    }
