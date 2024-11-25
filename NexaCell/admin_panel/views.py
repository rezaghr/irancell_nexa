from django.shortcuts import render, HttpResponse
from admin_panel.models import PhoneNumber

def showform(request): 
    return render(request, "showform.html") 

from django.shortcuts import render
from admin_panel.models import PhoneNumber

def getscore(request): 
    if request.method == "POST": 
        phone_number = request.POST.get('phone_number')  # Safely get the phone number
        try:
            # Look up the PhoneNumber object
            phone_number_obj = PhoneNumber.objects.get(phone_number=phone_number)
            
            # Get the associated user's loyalty tokens
            user = phone_number_obj.user
            loyalty_tokens = user.loyalty_tokens
            
            # Pass data to the template
            context = {
                'phone_number': phone_number,
                'user_name': user.name,
                'loyalty_tokens': loyalty_tokens,
                'error': None
            }
        except PhoneNumber.DoesNotExist:
            # Handle case where the phone number is not found
            context = {
                'phone_number': phone_number,
                'user_name': None,
                'loyalty_tokens': None,
                'error': f"شماره {phone_number} یافت نشد."
            }
    else:
        # For non-POST requests, return an error
        context = {
            'phone_number': None,
            'user_name': None,
            'loyalty_tokens': None,
            'error': "فقط درخواست‌های POST پذیرفته می‌شوند."
        }

    return render(request, 'showscore.html', context)
