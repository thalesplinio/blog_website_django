from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup


# Register your models here.
@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path',
    search_fields = 'id', 'text', 'url_or_path',
    list_display_links = 'id', 'text',


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


# Register your models here.
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'site_name', 'title', 'description',
    list_display_links = 'site_name', 'title',
    inlines = MenuLinkInLine,

    # removendo a opção de adicionar mais de um setup
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
