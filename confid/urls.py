from django.contrib import admin
from django.urls import path
from page.views import hello_site



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello_site),

]
