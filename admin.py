from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fields = ("title", "parent", "url", "named_url", "order", "visible")
    ordering = ("order",)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = (MenuItemInline,)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "menu", "parent", "order", "visible")
    list_filter = ("menu", "visible")
    search_fields = ("title", "url", "named_url")
    ordering = ("menu", "order")
