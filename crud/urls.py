from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken import views

urlpatterns = [
    path('get-token/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/v1/recipes/',include("api.urls"))
]