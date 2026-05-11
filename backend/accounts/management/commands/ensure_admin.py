"""Idempotently create or refresh the project's grader/demo admin account.

Run from the project root:

    python manage.py ensure_admin

This is safe to run repeatedly. If the admin already exists, the password
and staff/superuser flags are reset to the documented defaults so a grader
can always log in with the credentials in README.md.

Defaults can be overridden with CLI flags or environment variables:

    --username  / DJANGO_ADMIN_USERNAME   (default: IS218)
    --password  / DJANGO_ADMIN_PASSWORD   (default: ProjectIS218)
    --email     / DJANGO_ADMIN_EMAIL      (default: admin@example.com)
"""

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


DEFAULT_USERNAME = "IS218"
DEFAULT_PASSWORD = "ProjectIS218"
DEFAULT_EMAIL = "admin@example.com"


class Command(BaseCommand):
    help = (
        "Create or refresh the demo/grader admin account "
        "(default: IS218 / ProjectIS218)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            default=os.environ.get("DJANGO_ADMIN_USERNAME", DEFAULT_USERNAME),
            help="Username for the admin account.",
        )
        parser.add_argument(
            "--password",
            default=os.environ.get("DJANGO_ADMIN_PASSWORD", DEFAULT_PASSWORD),
            help="Password for the admin account.",
        )
        parser.add_argument(
            "--email",
            default=os.environ.get("DJANGO_ADMIN_EMAIL", DEFAULT_EMAIL),
            help="Email address for the admin account.",
        )

    def handle(self, *args, **options):
        User = get_user_model()
        username = options["username"]
        password = options["password"]
        email = options["email"]

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email},
        )
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(
            f"{action} admin '{username}' (staff=True, superuser=True). "
            f"Sign in at /admin/ with username '{username}'."
        ))
