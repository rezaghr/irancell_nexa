from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1  # Allows adding one extra phone number in the admin panel


class UserAdmin(admin.ModelAdmin):
    # Customize the display of fields in the admin panel
    list_display = (
        'name',
        'number_of_phone_numbers',
        'in_app_transaction',
        'bought_pakage_amount',
        'shop_transaction',
    )
    list_filter = ('bought_pakage_amount', 'shop_transaction')  # Add filters for specific fields
    search_fields = ('name',)  # Enable search functionality for the 'name' field

    # Add inlines to manage phone numbers directly within the User admin
    inlines = [PhoneNumberInline]

    # Provide help text for each field in the admin panel
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # Define help texts for fields
        help_texts = {
            'name': 'Full name of the user.',
            'in_app_transaction': 'Total number of transactions made within the app.',
            'bought_pakage_amount': 'Amount spent by the user on purchased packages.',
            'shop_transaction': 'Total number of transactions made at physical or online shops.',
        }
        if db_field.name in help_texts:
            kwargs['help_text'] = help_texts[db_field.name]
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    # Custom method to count the number of phone numbers for a user
    def number_of_phone_numbers(self, obj):
        return obj.phone_numbers.count()

    # Rename the column in the admin panel for better clarity
    number_of_phone_numbers.short_description = 'Phone Numbers'


# Register the models with the admin panel
admin.site.register(User, UserAdmin)
admin.site.register(PhoneNumber)
