from django.test import TestCase

from .helpers import VALID, User, make_user  # noqa: F401


class ModelTests(TestCase):
    def test_createsuperuser_gets_admin_role(self):
        su = User.objects.create_superuser("root", "root@example.com", "Sup3r-secret-pw")
        self.assertEqual(su.role, User.Role.ADMIN)

    def test_db_enforces_unique_email_ci(self):
        from django.db import IntegrityError, transaction
        make_user("a", email="x@example.com")
        with self.assertRaises(IntegrityError), transaction.atomic():
            User.objects.create_user("b", email="X@EXAMPLE.COM", password="Sup3r-secret-pw")