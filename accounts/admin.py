from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "member_type", "is_active", "date_joined")
    list_filter = ("role", "member_type", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("ShareShelf", {"fields": ("role", "member_type", "contact_number", "address", "bio", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "role", "member_type")}),
    )