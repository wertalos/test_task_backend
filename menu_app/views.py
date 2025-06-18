from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    # Get menu_name from query params or default to showing all menus
    menu_name = request.GET.get('menu_name')
    
    # Get all menu items if no specific menu is requested
    if menu_name:
        menu_items = MenuItem.objects.filter(menu_name=menu_name)
    else:
        menu_items = MenuItem.objects.all()
    
    # Get unique menu names for navigation
    menu_names = MenuItem.objects.values_list('menu_name', flat=True).distinct()
    
    context = {
        'menu_items': menu_items,
        'menu_name': menu_name,
        'menu_names': menu_names,
    }
    return render(request, 'menu_app/menu.html', context)