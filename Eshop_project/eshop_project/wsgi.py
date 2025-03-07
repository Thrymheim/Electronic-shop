import os
import sys

path = '/home/yourusername/your-portfolio-repo'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
