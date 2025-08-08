#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracewizesolutions.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Auto-create superuser if it doesn't exist
    from django.core.management import call_command
    import django
    django.setup()
    from django.contrib.auth import get_user_model

    User = get_user_model()
    if not User.objects.filter(username="mmaleka2").exists():
        print("🔐 Creating default superuser...")
        User.objects.create_superuser(
            username="mmaleka2",
            email="mmaleka@example.com",
            password="Mpho@@6829"
        )
        print("✅ Superuser created.")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
