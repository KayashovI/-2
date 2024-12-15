from django.urls import path
from .views import login_view, admin_page, user_page, register_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('admin_page/', admin_page, name='admin_page'),
    path('user_page/', user_page, name='user_page'),
    path('logout/', logout_view, name='logout'),  # Маршрут для выхода
]