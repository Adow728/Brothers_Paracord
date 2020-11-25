from django.shortcuts import render
from django.db.models import Sum

from .models import Color, Order, Product, Sale, Material, StoreProduct
from .queries import find_capital

# Create your views here.

# Read views
def manage(request):
    orders = Order.objects.order_by("due_date")
    colors = Color.objects.order_by("name")
    num_products = len(Product.objects.all())
    total_sales = Sale.objects.aggregate(Sum("revenue"))["revenue__sum"]
    total_expenses = Material.objects.aggregate(Sum("price"))["price__sum"]
    gain = total_sales - total_expenses
    capital = find_capital()

    context = {
        "orders":orders, 
        "colors":colors,
        "products":num_products,
        "sales":total_sales,
        "expenses":total_expenses,
        "gain":gain,
        "capital":capital
    }

    return render(request, "management/dashboard.html", context)

def products(request):
    products = Product.objects.order_by("name")

    context = {
        "products":products
    }

    return render(request, "management/products.html", context)

def product(request, id):
    product = Product.objects.get(id=id)

    context = {
        "product":product
    }

    return render(request, "management/product.html", context)

def order(request, id):
    order = Order.objects.get(id=id)
    info_string = order.customer.full_name + " - " + str(order.due_date)
    items = order.item_set.all()
    
    context = {
        "order":order,
        "info_string":info_string,
        "items":items
    }

    return render(request, "management/order.html", context)

def complete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    