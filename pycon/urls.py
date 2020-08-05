from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', include('apps.store.urls')),
    path('pycon_base_admin/', admin.site.urls)
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ]