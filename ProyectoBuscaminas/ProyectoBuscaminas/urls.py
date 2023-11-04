from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buscaminas1/', include('buscaminas1.urls')),
    path('', include('buscaminas1.urls'))
]
