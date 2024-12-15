from django.contrib.auth.backends import BaseBackend
from .models import Users

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Users.objects.get(Username=username)
            if user.check_password(password):  # Проверяем хешированный пароль
                return user
        except Users.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None