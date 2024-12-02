from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Incluye las rutas de la app "blog"
]

# Configura las rutas para archivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Configura las rutas para archivos de medios (ya lo tienes bien)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
