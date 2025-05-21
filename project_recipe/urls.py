from django.contrib import admin
from django.urls import path
from recipe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
]