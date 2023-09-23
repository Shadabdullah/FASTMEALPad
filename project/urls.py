
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('getmealfast-shad-admin/', admin.site.urls),
    path('', include("base.urls")),
   
]

