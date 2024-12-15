from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='home'),  # Перенаправление на страницу входа
    path('', include('myapp.urls')),  # Подключение маршрутов приложения
]