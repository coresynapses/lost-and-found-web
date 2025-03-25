from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Item

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
        "is_active",
    ]

class ItemAdmin(admin.ModelAdmin):
    list_display =["itemName","category","status","dateReported","location", "photo"]
    list_filter = ["status","category"]
    search_fields = ["itemName","description","location"]

admin.site.register(Item, ItemAdmin)
admin.site.register(CustomUser,CustomUserAdmin)