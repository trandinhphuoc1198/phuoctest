
from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register,name='register'),
    path('update-profile', views.update_profile,name='update_profile'),
    path('profile', views.profile,name='profile'),
    path('logout', views.logout_view,name='logout'),
    path('login', views.login_view,name='login')
]
