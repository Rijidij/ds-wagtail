from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@6gce61jt^(pyj5+l**&*_#zyxfj5v1*71cs5yoetg-!fsz826'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    "wagtail.contrib.styleguide",
    "debug_toolbar"
]


def show_toolbar_callback(request):
    """Override debug_toolbar's show_toolbar_callback which by default checks
    whether the current IP is within INTERNAL_IPS. Unfortunately, the REMOTE_ADDR
    is Docker's bridge IP and not localhost or 0.0.0.0
    """

    return True

    import sys

    if "manage.py" in sys.argv:
        """Don't show debug toolbar if django is being exectuted via manage.py"""
        return False

    return strtobool(os.getenv("SHOW_DEBUG_TOOLBAR", "False"))


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar_callback}

MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]
