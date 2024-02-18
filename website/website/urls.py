
from django.contrib import admin
from django.urls import path
from arada.views import home, product, contact
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('contact/',contact, name = 'contact'),
    path('product/', product, name = 'product')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)