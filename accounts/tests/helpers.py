from django.contrib.auth import get_user_model

User = get_user_model()

VALID = {
    "first_name": "Juan",
    "last_name": "Dela Cruz",
    "username": "juandc",
    "email": "juan@example.com",
    "contact_number": "0917 123 4567",
    "member_type": "both",
    "password1": "Sup3r-secret-pw",
    "password2": "Sup3r-secret-pw",
}


def make_user(username="maria", role=User.Role.MEMBER, password="Sup3r-secret-pw", **kw):
    return User.objects.create_user(
        username=username, email=kw.pop("email", f"{username}@example.com"),
        password=password, role=role, first_name=kw.pop("first_name", username.title()), **kw,
    )