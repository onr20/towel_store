from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('products.urls')),
    path("basket/", include("orders.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

