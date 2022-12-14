from django.urls import path
from .views import index, RegisterUser, LoginUser, logout_user
urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
