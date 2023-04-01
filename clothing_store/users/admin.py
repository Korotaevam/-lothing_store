from django.contrib import admin
from store_main.admin import BasketAdminInline
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
