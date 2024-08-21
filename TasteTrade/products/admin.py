from django.contrib import admin
from .models import Category


# Register your models here.


#supplier_group, created = Group.objects.get_or_create(name='Supplier')


#permissions = Permission.objects.filter(content_type__app_label='yourapp', codename__in=['add_product', 'change_product', 'delete_product'])
#supplier_group.permissions.set(permissions)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
