from django.contrib import admin
from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'default_phone_number')
    # Add any other fields you want to display in the admin list view

    # Customize the fields displayed in the detail view
    fieldsets = (
        ('User Profile', {
            'fields': ('user', 'name')
        }),
        ('Default Delivery Information', {
            'fields': ('default_phone_number', 'default_street_address1', 'default_street_address2',
                       'default_town_or_city', 'default_county', 'default_postcode', 'default_country')
        }),
    )

    # Customize the filter options in the admin list view
    list_filter = ('default_country',)