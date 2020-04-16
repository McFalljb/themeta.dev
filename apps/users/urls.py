"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
#from .views import UserProfileDetailView, PostListView

urlpatterns = [
    #path('users/<str:display_name>/', UserProfileDetailView.as_view(), name='user_profile'),
    path('users/<str:display_name>/', views.get_user_profile, name='user_profile'),
    #path('users/<str:display_name>/', views.UserProfile, name='user_profile'),
    #path('users/profile/', views.UserProfile, name='user_profile'),  

    #path('users/profile_edit/', views.UserEditProfile, name='profile_edit'),
    path('users/profile_edit/<str:display_name>', views.UserEditProfile, name='profile_edit'),
    
]
