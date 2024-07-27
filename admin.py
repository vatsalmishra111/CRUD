from django.contrib import admin

# Register your models here.
from .models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone')  # Customize as needed

admin.site.register(Employees, EmployeesAdmin)
