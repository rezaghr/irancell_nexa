from django.urls import path
from .views import showform
urlpatterns = [
    path("showform/", showform, name="showform"), 
    # path("getscore/", views.getform, name='getscore'),
]