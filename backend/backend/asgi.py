import os
from django.core.asgi import get_asgi_application
import zoom_connection.routing  # This works if folder is in the right place

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()
