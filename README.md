
# 🧭 Django Tree Menu App

A reusable **Django app** that implements a dynamic, tree-structured menu rendered via a **custom template tag** — following the technical requirements of a test assignment.

---

## 🚀 Features

✅ Menu structure stored in the database (via Django models)  
✅ Fully editable in Django Admin  
✅ Menu rendered using a **single database query**  
✅ Supports multiple menus on the same page  
✅ Highlights the **active item** based on the current URL  
✅ Expands all parent items and the first level under the active item  
✅ Supports both **explicit URLs** and **named Django URLs**  
✅ Implemented only with **Django + Python standard library**

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/smailxpy/django-tree-menu.git
   cd django-tree-menu
Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run initial migrations

python manage.py makemigrations tree_menu
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the server

python manage.py runserver


Open admin panel
Go to: http://127.0.0.1:8000/admin

Create a Menu (e.g., main_menu)

Add several Menu Items with hierarchy (using the parent field)

💡 Usage

In your Django template:

{% load menu_tags %}
{% draw_menu 'main_menu' %}


Make sure your view uses render(request, "template.html") so the request context is available.

🧩 Example Structure

Menu: main_menu

Title	Parent	URL / Named URL	Order
Home	—	/	1
Catalog	—	catalog:index	2
Category A	Catalog	catalog:category_a	1
Category B	Catalog	catalog:category_b	2
About	—	/about/	3
📂 Folder Structure
tree_menu/
├── admin.py
├── apps.py
├── models.py
├── templatetags/
│   └── menu_tags.py
└── templates/
    └── tree_menu/
        ├── menu.html
        └── menu_item.html

🧠 Technical Notes

Only 1 SQL query is executed to load the entire menu.

The active menu item is matched by request.path.

Parent nodes of the active item are automatically expanded.

The first level of children under the active node is expanded too.

Uses only Django + Python standard library (no third-party packages).

🧑‍💻 Author

Ismoil Salohiddinov
GitHub: @smailxpy

Telegram: @clbrex

⚖️ License

MIT License – free to use and modify.

📦 requirements.txt
Django>=4.2,<5.0


---

✅ Just paste this full text into your `README.md` file  
Then run:
```bash
git add README.md
git commit -m "Add README and requirements section"
git push
