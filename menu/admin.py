from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('title', 'url', 'named_url', 'parent', 'order')
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'order', 'url', 'named_url')
    list_filter = ('menu', 'parent')
    list_editable = ('order',)
    search_fields = ('title', 'url', 'named_url')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('menu', 'parent')
