from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'get_html_photo')

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=30>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Миниатюра"


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
