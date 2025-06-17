from django import template
from django.db.models import Prefetch
from django.urls import resolve, Resolver404
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    
    request = context['request']
    current_url = request.path
    
    try:
        menu = Menu.objects.prefetch_related(
            Prefetch('items', queryset=MenuItem.objects.select_related('parent'))
        ).get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': [], 'current_url': current_url}
    
    all_items = {item.id: item for item in menu.items.all()}
    
    active_item = None
    for item in all_items.values():
        item_url = item.get_url()
        if item_url == current_url or (item_url != '#' and current_url.startswith(item_url) and len(item_url) > 1):
            active_item = item
            break
    
    
    expanded_items = set()
    if active_item:
        
        current = active_item
        while current:
            expanded_items.add(current.id)
            current = current.parent
        
        for item in all_items.values():
            if item.parent_id == active_item.id:
                expanded_items.add(item.id)
    
    def build_tree_items(parent_id=None):
        items = []
        for item in all_items.values():
            if item.parent_id == parent_id:
                should_show = (
                    parent_id is None or 
                    item.parent_id in expanded_items 
                )
                
                if should_show:
                    children = build_tree_items(item.id)
                    items.append({
                        'item': item,
                        'children': children,
                        'is_active': item.id == (active_item.id if active_item else None),
                        'is_expanded': item.id in expanded_items,
                        'has_children': bool(children) or any(
                            child.parent_id == item.id for child in all_items.values()
                        )
                    })
        return items
    
    menu_items = build_tree_items()
    
    return {
        'menu_items': menu_items,
        'current_url': current_url,
        'menu_name': menu_name
    } 