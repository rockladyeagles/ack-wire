"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acquire.settings")
os.environ['ASGI_THREADS'] = "1"
django.setup()
application = get_default_application()
