from django.shortcuts import render
from django.db.models import Sum

from .models import Color, Order, Product, Sale, Material, StoreProduct
from .queries import find_capital

# Create your views here.

def manage(request):
    orders = Order.objects.order_by("due_date")
    colors = Color.objects.order_by("name")
    num_products = len(Product.objects.all())
    total_sales = Sale.objects.aggregate(Sum("revenue"))["revenue__sum"]
    total_expenses = Material.objects.aggregate(Sum("price"))["price__sum"]
    gain = total_sales - total_expenses
    capital = find_capital()

    context = {"orders":orders, 
               "colors":colors,
               "products":num_products,
               "sales":total_sales,
               "expenses":total_expenses,
               "gain":gain,
               "capital":capital
              }

    return render(request, "brothers_paracord/dashboard.html", context=context)