from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/v1/', include('user.urls')),
    # path('api/v1/', include('authenticate.urls')),
    path('api/v1/', include('region.urls')),
    path('api/v1/', include('area.urls')),
    path('api/v1/', include('faculty.urls')),
    path('api/v1/', include('student.urls')),
]
