from django.contrib import admin
from .models import Doctor


class ProductAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(Doctor)
