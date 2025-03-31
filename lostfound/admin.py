from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Item, claimRequestReport, fraudClaimReport

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
        (None, {"fields": ("username","first_name","last_name", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    
    add_fieldsets = (
        (None, {"fields": ("username","first_name","last_name", "email", "password1", "password2")}),
    )

class itemAdmin(admin.ModelAdmin):
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
    list_per_page = 20

class claimRequestAdmin(admin.ModelAdmin):
    list_display = [
        "status",
        "item",
        "claimer",
        "dateSubmitted",
        "dateReviewed",
        "reviewAdmin",
    ]
    list_filter = [
        "status",
        "claimer",
        "reviewAdmin",
    ]
    search_fields = [
        "item__itemName",
        "claimer__username",
        "reviewAdmin__username",
    ]
    fields = [
        "item",
        "status",
        "claimer",
        "proofOfOwnership",
        "dateReviewed",
        "reviewAdmin",
    ]
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if obj.status == obj.approved:
            obj.approveClaim(adminUser=request.user) #update the item status

        super().save_model(request, obj, form, change)

class fraudClaimAdmin(admin.ModelAdmin):
    list_display = [
        "status",
        "item",
        "reporter",
        "dateSubmitted",
        "dateReviewed",
        "reviewAdmin",
    ]
    list_filter =[
        "status",
        "reporter",
        "reviewAdmin",
    ]
    search_fields = [
        "item__itemName",
        "reporter__username",
        "reviewAdmin__username",
    ]
    field = [
        "item",
        "status",
        "reporter",
        "proofOfOwnership",
        "dateReviewed",
        "reviewAdmin",
    ]

admin.site.register(Item, itemAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(claimRequestReport, claimRequestAdmin)
admin.site.register(fraudClaimReport, fraudClaimAdmin)