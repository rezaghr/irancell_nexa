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
        'social_number',
        'name',
        'number_of_phone_numbers',
        'in_app_transaction',
        'bought_pakage_amount',
        'shop_transaction',
        'loyalty_tokens',
    )
    # list_filter = ('loyalty_tokens',)  # Add filters for specific fields
    search_fields = ('name',)  # Enable search functionality for the 'name' field
    ordering = ('-loyalty_tokens',)
    # Add inlines to manage phone numbers directly within the User admin
    inlines = [PhoneNumberInline]

    # Provide help text for each field in the admin panel
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # Define help texts for fields
        help_texts = {
            'social_number': 'کد ملی',
            'name': 'نام و نام خانوادگی',
            'in_app_transaction': 'حجم پرداختی های درون برنامه ای',
            'bought_pakage_amount': 'حجم پرداختی پکیج های خریداری شده',
            'shop_transaction': 'مبلغ خریداری شده از فروشگاه',
        }
        if db_field.name in help_texts:
            kwargs['help_text'] = help_texts[db_field.name]
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    # Custom method to count the number of phone numbers for a user
    def number_of_phone_numbers(self, obj):
        return obj.phone_numbers.count()

    # Rename the column in the admin panel for better clarity
    number_of_phone_numbers.short_description = 'شماره تماس'
    
    # Method to calculate the total transactions for display in the admin panel
    def total_transactions(self, obj):
        return obj.in_app_transaction + obj.bought_pakage_amount + obj.shop_transaction
    total_transactions.short_description = 'Total Transactions'

# Register the models with the admin panel
admin.site.register(User, UserAdmin)
admin.site.register(PhoneNumber)
