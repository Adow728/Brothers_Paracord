from django.db.models import Sum

from .models import Material, StoreProduct

# Create your queries here

def find_capital():
    subtotal = Material.objects.filter(expended=False).aggregate(Sum("price"))["price__sum"]
    for product in StoreProduct.objects.all():
        subtotal += product.value

    return subtotal