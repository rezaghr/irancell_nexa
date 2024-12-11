from django.urls import path
from .views import showform, getscore, top_users
app_name = 'admin_panel'
urlpatterns = [
    path("showform/", showform, name="showform"), 
    path("getscore/", getscore, name='getscore'),
    path("top/", top_users, name='top_10_user')
]