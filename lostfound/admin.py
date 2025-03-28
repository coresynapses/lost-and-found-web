from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Item, Category

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
        "is_active",
        "last_login",
        "date_joined",
    ]

    fieldsets = (
        (None, {"fields": ("username","first_name","last_name", "email", "password1", "password2")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    
    add_fieldsets = (
        (None, {"fields": ("username","first_name","last_name", "email", "password1", "password2")}),
    )

class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "itemName",
        "category",
        "status",
        "dateReported",
        "location",
        "photo",  # Kept from your version
    ]
    list_filter = [
        "status",
        "category",
    ]
    search_fields = [
        "itemName",
        "description",
        "location",
    ]
    fields = [
        "itemName",
        "description",
        "category",
        "location",
        "status",
        "contactInfo",  # Andres's updates
        "photo",  # Andrew's Updates
    ]

   # @admin.register(Category)
   # class CategoryAdmin(admin.ModelAdmin):
    #    list_display = ('id', 'name')  # Ensure it's visible in the admin panel

admin.site.register(Item, ItemAdmin)
admin.site.register(CustomUser,CustomUserAdmin)

#meow