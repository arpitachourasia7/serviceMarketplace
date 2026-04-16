from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),

]