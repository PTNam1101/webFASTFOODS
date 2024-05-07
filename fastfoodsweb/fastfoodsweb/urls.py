from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

admin.site.site_header = 'Quản lý FASTFOODS'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webstore.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        
        
        