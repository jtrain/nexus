import os
from django.conf import settings

MEDIA_PREFIX = getattr(settings, 'NEXUS_MEDIA_PREFIX', '/nexus/media/')

if getattr(settings, 'NEXUS_USE_DJANGO_MEDIA_URL', False):
    MEDIA_PREFIX = getattr(settings, 'MEDIA_URL', MEDIA_PREFIX)

USE_STATICFILES = getattr(settings, 'NEXUS_USE_STATICFILES', False)

if USE_STATICFILES:
    nexus_static = (
        ('nexus', os.path.join(os.path.dirname(__file__),
                                              'media')),
    )
    if isinstance(settings.STATICFILES_DIRS, tuple):
       settings.STATICFILES_DIRS += nexus_static
    else:
       settings.STATICFILES_DIRS.extends(nexus_static)
