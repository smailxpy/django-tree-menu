from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Short unique menu name (used in template tag)")

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField("explicit URL", max_length=500, blank=True, help_text="Absolute or relative path e.g. /about/")
    named_url = models.CharField("named URL", max_length=255, blank=True, help_text="Django named URL (reverse name)")
    order = models.IntegerField(default=0, help_text="Order among siblings: smaller first")
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ("order", "id")
        verbose_name = "Menu item"
        verbose_name_plural = "Menu items"

    def __str__(self):
        return self.title
