from django.contrib import admin
from .models import Product
from .models import Car
from .models import Student

# Register your models here.
admin.site.register(Product)
admin.site.register(Car)
admin.site.register(Student)