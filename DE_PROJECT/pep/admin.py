from django.contrib import admin
from .models import service_reg , reg_service_provider

# Register your models here.
admin.site.register(service_reg)
admin.site.register(reg_service_provider)