from django.shortcuts import render
from admin_panel.models import User

def showform(request): 
    return render(request, "showform.html") 

# def getscore(request): 
#     if request.method == "POST": 
#         phone_number =request.POST['phone_number'] 
#     return render("Name:{} UserID:{}".format(name, id)) 