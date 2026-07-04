from django.contrib import admin
from django.urls import path

from page.views import get_product, detail_product, create_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_product, name='list'),
    path('detail/<int:pk>/', detail_product, name='detail'),
    path('create/', create_product, name='create'),
]
