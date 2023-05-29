from django.urls import path
from . import views

from django.contrib.auth import views as auth_view
app_name='users'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('logout',auth_view.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
]

