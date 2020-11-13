from django.contrib import admin

# Register your models here.

from management.models import Product, Material, Color, ProductColorSlot, Customer, StoreProduct
from management.models import Sale, StoreSale, Employee, Order, Item, ItemColor

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(ProductColorSlot)
admin.site.register(Customer)
admin.site.register(StoreProduct)
admin.site.register(Sale)
admin.site.register(StoreSale)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(ItemColor)