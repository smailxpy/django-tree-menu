from django import template
from django.urls import reverse, NoReverseMatch
from ..models import MenuItem, Menu

register = template.Library()

@register.inclusion_tag("tree_menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context.get("request")
    if request is None:
        raise RuntimeError("draw_menu requires 'request' in the template context (use RequestContext).")

    items_qs = MenuItem.objects.filter(menu__name=menu_name, visible=True).order_by("order", "id")
    items = list(items_qs)

    nodes = {}
    for it in items:
        nodes[it.id] = {
            "obj": it,
            "children": [],
            "parent_id": it.parent_id,
            "target_path": None,
            "active": False,
            "expanded": False,
        }

    roots = []
    for it in items:
        node = nodes[it.id]
        pid = node["parent_id"]
        if pid and pid in nodes:
            nodes[pid]["children"].append(node)
        else:
            roots.append(node)

    for n in nodes.values():
        obj = n["obj"]
        path = None
        if obj.named_url:
            try:
                path = reverse(obj.named_url)
            except NoReverseMatch:
                path = None
        if not path and obj.url:
            path = obj.url
        n["target_path"] = path

    current = request.path
    active_node = None
    best_len = -1
    for n in nodes.values():
        tp = n["target_path"]
        if not tp:
            continue
        if current == tp:
            active_node = n
            best_len = len(tp or "")
            break
        if current.startswith(tp) and len(tp) > best_len:
            active_node = n
            best_len = len(tp)

    if active_node:
        active_node["active"] = True
        parent_id = active_node["parent_id"]
        while parent_id:
            parent_node = nodes.get(parent_id)
            if not parent_node:
                break
            parent_node["expanded"] = True
            parent_id = parent_node["parent_id"]
        active_node["expanded"] = True
        for child in active_node["children"]:
            child["expanded"] = True

    def serialize(node):
        return {
            "title": node["obj"].title,
            "url": node["target_path"],
            "named_url": node["obj"].named_url,
            "children": [serialize(c) for c in node["children"]],
            "active": node["active"],
            "expanded": node["expanded"],
        }

    tree = [serialize(r) for r in roots]
    return {
        "menu_tree": tree,
        "menu_name": menu_name,
        "request": request,
    }
