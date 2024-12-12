from django.shortcuts import render, HttpResponse
from admin_panel.models import PhoneNumber, User

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
            
            # Get the associated user's data
            user = phone_number_obj.user
            loyalty_tokens = user.loyalty_tokens
            social_number = user.social_number  # Fetch social number from the user model

            # Calculate user rank based on loyalty tokens
            rank = User.objects.filter(loyalty_tokens__gt=loyalty_tokens).count() + 1

            # Find the user with the most loyalty tokens
            top_user = User.objects.order_by('-loyalty_tokens').first()
            is_top_user = user == top_user
            
            # Pass data to the template
            context = {
                'phone_number': phone_number,
                'user_name': user.name,
                'loyalty_tokens': loyalty_tokens,
                'social_number': social_number,
                'rank': rank,
                'is_top_user': is_top_user,
                'error': None
            }
        except PhoneNumber.DoesNotExist:
            # Handle case where the phone number is not found
            context = {
                'phone_number': phone_number,
                'user_name': None,
                'loyalty_tokens': None,
                'social_number': None,
                'rank': None,
                'is_top_user': False,
                'error': f"شماره {phone_number} یافت نشد."
            }
    else:
        # For non-POST requests, return an error
        context = {
            'phone_number': None,
            'user_name': None,
            'loyalty_tokens': None,
            'social_number': None,
            'rank': None,
            'is_top_user': False,
            'error': "فقط درخواست‌های POST پذیرفته می‌شوند."
        }

    return render(request, 'showscore.html', context)

def top_users(request):
    # Fetch the top 10 users based on loyalty tokens
    top_users = User.objects.order_by('-loyalty_tokens')[:10]
    print(top_users)
    # Render the data in a template
    return render(request, 'top_users.html', {'top_users': top_users})
