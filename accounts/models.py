from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.functions import Lower


class CustomUserManager(UserManager):
    """Superusers created via `createsuperuser` automatically get the Admin role."""

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("role", User.Role.ADMIN)
        return super().create_superuser(username, email, password, **extra_fields)


contact_validator = RegexValidator(
    regex=r"^\+?[0-9][0-9\s\-]{6,18}$",
    message="Enter a valid contact number (digits, spaces or dashes; may start with +).",
)


class User(AbstractUser):
    """ShareShelf user. Passwords are hashed by Django's auth system."""

    class Role(models.TextChoices):
        ADMIN = "admin", "Admin (Community Moderator)"
        MEMBER = "member", "Member (Lender / Borrower)"

    class MemberType(models.TextChoices):
        LENDER = "lender", "Lender"
        BORROWER = "borrower", "Borrower"
        BOTH = "both", "Both"

    # Role decides which dashboard a user can open. Never editable by the user.
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)

    # What the member does in the community (from the proposal: "lender, borrower, or both").
    member_type = models.CharField(max_length=10, choices=MemberType.choices, default=MemberType.BOTH)

    email = models.EmailField("email address", unique=True)
    contact_number = models.CharField(max_length=20, blank=True, validators=[contact_validator])
    address = models.CharField("barangay / address", max_length=255, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        constraints = [
            # Case-insensitive uniqueness: Juan@x.com and juan@x.com are the same email.
            models.UniqueConstraint(Lower("email"), name="unique_user_email_ci"),
        ]

    @property
    def is_admin_role(self):
        return self.role == self.Role.ADMIN

    @property
    def display_name(self):
        return self.get_full_name() or self.username

    def __str__(self):
        return self.username