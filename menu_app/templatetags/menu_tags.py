from django import template
from django.utils.html import format_html
from menu_app.models import MenuItem
from django.db.models import Prefetch

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Renders a menu with the specified name, handling active states and parent expansion.
    """
    current_url = context['request'].path

    # Get all menu items for this menu
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('order')
    
    if not menu_items.exists():
        return ''  # Return empty string if no menu items exist
    
    # Create a dict for quick lookup of items by id
    items_dict = {item.id: item for item in menu_items}
    
    # Create a dict to store parent-child relationships
    children_dict = {}
    root_items = []
    
    # Organize items into hierarchy
    for item in menu_items:
        if item.parent_id is None:
            root_items.append(item)
        else:
            if item.parent_id not in children_dict:
                children_dict[item.parent_id] = []
            children_dict[item.parent_id].append(item)
    
    # Find active item and its ancestors
    active_ancestors = set()
    for item in menu_items:
        if item.get_url() == current_url:
            current = item
            while current is not None:
                active_ancestors.add(current.id)
                current = current.parent

    def build_menu_level(items, level=0):
        if not items:
            return ""

        menu_html = []
        menu_html.append(f'<ul class="menu-level-{level}" role="menu">')

        for item in items:
            is_active = item.id in active_ancestors
            is_current = item.get_url() == current_url
            has_children = item.id in children_dict

            # Build CSS classes
            classes = []
            if is_current:
                classes.append('current')
            if is_active:
                classes.append('active')
            if has_children:
                classes.append('has-submenu')
                if is_active:
                    classes.append('expanded')

            menu_html.append(f'<li class="{" ".join(classes)}" role="presentation">')
            
            # For items with children, use a button instead of a link
            if has_children:
                menu_html.append(
                    f'<button type="button" class="menu-toggle" '
                    f'aria-haspopup="true" '
                    f'aria-expanded="{"true" if is_active else "false"}" '
                    f'aria-controls="submenu-{item.id}" '
                    f'role="menuitem">'
                    f'{item.title}'
                    f'</button>'
                )
            else:
                # Regular link for items without children
                menu_html.append(
                    f'<a href="{item.get_url()}" role="menuitem">'
                    f'{item.title}'
                    f'</a>'
                )

            # Recursively add children
            if has_children:
                submenu_classes = ["submenu", f"submenu-level-{level}"]
                menu_html.append(f'<ul id="submenu-{item.id}" class="{" ".join(submenu_classes)}" role="menu">')
                menu_html.append(build_menu_level(children_dict[item.id], level + 1))
                menu_html.append('</ul>')

            menu_html.append('</li>')

        menu_html.append('</ul>')
        return "".join(menu_html)

    # Start building from root items
    return format_html(build_menu_level(root_items))