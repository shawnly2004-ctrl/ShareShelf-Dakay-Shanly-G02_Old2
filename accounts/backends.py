from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameBackend(ModelBackend):
    """Lets users sign in with either their username or their email address."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if not username or not password:
            return None
        field = "email__iexact" if "@" in username else "username__iexact"
        try:
            user = User.objects.get(**{field: username})
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            User().set_password(password)  # equalise timing to avoid user enumeration
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None