from django.shortcuts import render
from django.db.models import Sum

from .models import Color, Employee, Order, Product, Sale, Material, StoreProduct
from .queries import find_capital
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# Read views
def manage(request):
    orders = Order.objects.order_by("due_date")
    colors = Color.objects.order_by("name")
    employees = Employee.objects.order_by("amount_owed").reverse()
    num_products = len(Product.objects.all())
    total_sales = Sale.objects.aggregate(Sum("revenue"))["revenue__sum"]
    total_expenses = Material.objects.aggregate(Sum("price"))["price__sum"]
    gain = total_sales - total_expenses
    capital = find_capital()

    context = {
        "orders":orders, 
        "colors":colors,
        "employees":employees,
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

def employee(request, id):
    employee = Employee.objects.get(id=id)
    outstanding_items = employee.employeebuild_set.filter(verified=False).order_by("date_completed")

    context = {
        "employee":employee,
        "outstanding_items":outstanding_items
    }
    return render(request, "management/employee.html", context)

def sales(request):
    sales = Sale.objects.order_by("date")

    context = {
        "sales":sales
    }

    return render(request, "management/sales.html", context)

# Add sale view here later

def expenses(request):
    expenses = Material.objects.order_by("date_bought")
    total_expenses = Material.objects.aggregate(Sum("price"))["price__sum"]

    context = {
        "expenses":expenses,
        "total_expenses":total_expenses
    }

    return render(request, "management/expenses.html", context)