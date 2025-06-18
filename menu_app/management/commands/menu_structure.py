from django.core.management.base import BaseCommand
from django.db import transaction
from menu_app.models import MenuItem

class Command(BaseCommand):
    help = 'Create initial menu structure'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        try:
            # Clear existing menu items
            MenuItem.objects.all().delete()

            # Create the initial menu structure
            self.create_menu_structure()
            self.stdout.write(self.style.SUCCESS('Successfully created initial menu structure'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating menu structure: {str(e)}'))

    def create_menu_structure(self):
        # Create main menu root items
        main_items = [
            MenuItem(title="Home", menu_name="main_menu", url="/", order=1),
            MenuItem(title="Products", menu_name="main_menu", url="/products/", order=2),
            MenuItem(title="Services", menu_name="main_menu", url="/services/", order=3),
            MenuItem(title="About Us", menu_name="main_menu", url="/about/", order=4),
        ]
        MenuItem.objects.bulk_create(main_items)
        
        # Create secondary menu root items
        secondary_items = [
            MenuItem(title="Support", menu_name="secondary_menu", url="/support/", order=1),
            MenuItem(title="Contact", menu_name="secondary_menu", url="/contact/", order=2),
            MenuItem(title="Resources", menu_name="secondary_menu", url="/resources/", order=3),
        ]
        MenuItem.objects.bulk_create(secondary_items)

        # Get parent items for creating submenus
        products = MenuItem.objects.get(title="Products", menu_name="main_menu")
        services = MenuItem.objects.get(title="Services", menu_name="main_menu")
        support = MenuItem.objects.get(title="Support", menu_name="secondary_menu")
        resources = MenuItem.objects.get(title="Resources", menu_name="secondary_menu")

        # Create Products submenu items
        product_items = [
            MenuItem(
                title="Electronics",
                menu_name="main_menu",
                parent=products,
                url="/products/electronics/",
                order=1
            ),
            MenuItem(
                title="Software",
                menu_name="main_menu",
                parent=products,
                url="/products/software/",
                order=2
            ),
            MenuItem(
                title="Accessories",
                menu_name="main_menu",
                parent=products,
                url="/products/accessories/",
                order=3
            ),
        ]
        MenuItem.objects.bulk_create(product_items)

        # Get Electronics item for its submenu
        electronics = MenuItem.objects.get(title="Electronics", parent=products)

        # Create Electronics submenu items
        electronics_items = [
            MenuItem(
                title="Laptops",
                menu_name="main_menu",
                parent=electronics,
                url="/products/electronics/laptops/",
                order=1
            ),
            MenuItem(
                title="Smartphones",
                menu_name="main_menu",
                parent=electronics,
                url="/products/electronics/smartphones/",
                order=2
            ),
            MenuItem(
                title="Tablets",
                menu_name="main_menu",
                parent=electronics,
                url="/products/electronics/tablets/",
                order=3
            ),
        ]
        MenuItem.objects.bulk_create(electronics_items)

        # Create Services submenu items
        service_items = [
            MenuItem(
                title="Consulting",
                menu_name="main_menu",
                parent=services,
                url="/services/consulting/",
                order=1
            ),
            MenuItem(
                title="Training",
                menu_name="main_menu",
                parent=services,
                url="/services/training/",
                order=2
            ),
        ]
        MenuItem.objects.bulk_create(service_items)

        # Create Support submenu items
        support_items = [
            MenuItem(
                title="FAQs",
                menu_name="secondary_menu",
                parent=support,
                url="/support/faqs/",
                order=1
            ),
            MenuItem(
                title="Documentation",
                menu_name="secondary_menu",
                parent=support,
                url="/support/docs/",
                order=2
            ),
        ]
        MenuItem.objects.bulk_create(support_items)

        # Create Resources submenu items
        resource_items = [
            MenuItem(
                title="Blog",
                menu_name="secondary_menu",
                parent=resources,
                url="/resources/blog/",
                order=1
            ),
            MenuItem(
                title="Downloads",
                menu_name="secondary_menu",
                parent=resources,
                url="/resources/downloads/",
                order=2
            ),
        ]
        MenuItem.objects.bulk_create(resource_items)