![Logo of the project](https://raw.githubusercontent.com/jehna/readme-best-practices/master/sample-logo.png)

# Django Tree Menu

> A Django application that implements a tree-like menu with dynamic rendering and smooth animations.

This project implements a Django-based tree menu system that can be easily integrated into any Django project. The menu supports unlimited nesting levels, dynamic expansion/collapse functionality, and smooth animations. It's built with modern web standards and is fully responsive.

## Features

* Tree-like menu structure with unlimited nesting levels
* Horizontal navigation bar with dropdown submenus
* Dynamic expansion/collapse functionality
* Smooth animations and transitions
* Responsive design that works on all devices
* Modern, clean UI with gradient backgrounds
* Accessible navigation with keyboard support
* Landing page with feature sections

## Tech Stack

* Python 3.x
* Django (Latest stable version)
* HTML5
* CSS3 (Modern features like Grid, Flexbox)
* JavaScript (Vanilla, no frameworks required)
* Font Awesome icons
* SQLite database

## Installing / Getting started

To get the project running, follow these steps:

```shell
# Clone the repository
git clone https://github.com/wertalos/test_task_backend.git
cd test_task_backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create initial menu structure
python manage.py menu_structure

# Run development server
python manage.py runserver
```

Visit http://localhost:8000/menu_app/menu/ to see the menu in action.

## Project Structure

```
test_task_backend/
├── menu_app/
│   ├── management/
│   │   └── commands/
│   │       └── menu_structure.py  # Command to create initial menu structure
│   ├── static/
│   │   └── menu_app/
│   │       └── css/
│   │           └── menu.css       # Menu styles and animations
│   ├── templates/
│   │   └── menu_app/
│   │       └── menu.html         # Main template with menu structure
│   ├── templatetags/
│   │   └── menu_tags.py         # Custom template tag for menu rendering
│   ├── models.py                # MenuItem model definition
│   ├── views.py                 # View logic
│   └── urls.py                  # URL configurations
└── test_task_backend/
    ├── settings.py              # Project settings
    └── urls.py                  # Project URL configurations
```

## Implementation Details

### Models

The menu structure is based on the `MenuItem` model with the following fields:
- `title`: Menu item text
- `url`: Link destination
- `menu_name`: Menu identifier (e.g., 'main_menu', 'secondary_menu')
- `parent`: Self-referential foreign key for nested structure
- `order`: Integer for custom ordering

### Template Tag

The custom template tag `draw_menu` handles:
- Recursive rendering of menu structure
- Active state tracking
- Parent-child relationships
- Dynamic expansion/collapse state

### Front-end Features

1. Navigation:
   - Fixed horizontal navigation bar
   - Dropdown menus on hover/click
   - Smooth transitions
   - Responsive mobile menu

2. Styling:
   - Modern gradient backgrounds
   - Card-based layout
   - Icon integration
   - Shadow effects
   - Hover animations

3. JavaScript Features:
   - Dynamic menu expansion/collapse
   - Keyboard navigation support
   - ARIA attributes for accessibility
   - Touch-friendly interactions

## Configuration

### MenuItem Configuration

```python
MenuItem(
    title="Products",      # Display text
    menu_name="main_menu", # Menu identifier
    url="/products/",      # URL path
    order=1,              # Display order
    parent=None           # Parent item (None for root items)
)
```

### Template Usage

```html
{% load menu_tags %}
{% draw_menu 'main_menu' %}  # Renders main navigation
{% draw_menu 'secondary_menu' %}  # Renders secondary navigation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[@wertalos](https://github.com/wertalos)
