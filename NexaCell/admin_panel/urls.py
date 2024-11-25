from django.urls import path
from .views import showform, getscore
app_name = 'admin_panel'
urlpatterns = [
    path("showform/", showform, name="showform"), 
    path("getscore/", getscore, name='getscore'),
]