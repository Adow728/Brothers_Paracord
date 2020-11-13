from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Product(models.Model):
    """The products we sell."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    order_cost = models.DecimalField(decimal_places=2, max_digits=4) # Price
    employee_payment = models.DecimalField(decimal_places=2, max_digits=4) # Price

    def __str__(self):
        return self.name

class Material(models.Model):
    """ A item we purchased to aid with production in some fashion."""
    name = models.CharField(max_length=200)
    date_bought = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2) # Price
    expended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Color(models.Model):
    """One of the paracord colors we make bracelets out of."""
    name = models.CharField(max_length=200)
    last_restock_length = models.IntegerField() # in Feet
    purchase_record = models.ForeignKey(Material, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class ProductColorSlot(models.Model):
    """A description of one of the place a color can be placed in a model."""
    name = models.CharField(max_length=200)
    approximate_length = models.IntegerField() # in feet
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    """Someone who purchases from our business"""
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11, blank=True, validators=[MinLengthValidator])
    address = models.TextField(max_length=1000, blank=True)
    email = models.EmailField(blank=True)
    normal_wrist_size = models.IntegerField(default=0) # in inches

    def __str__(self):
        return self.full_name

class StoreProduct(models.Model):
    """Records of inventory for products we sell at stores"""
    store = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_price = models.DecimalField(max_digits=4, decimal_places=2) # Price
    our_price = models.DecimalField(max_digits=4, decimal_places=2) # Price

    def __str__(self):
        return self.store.full_name + " - " + self.product.name

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=Product)
    date = models.DateField()
    revenue = models.DecimalField(max_digits=4, decimal_places=2) # Price

    def __str__(self):
        return self.customer.full_name + " - " + str(self.date)

class StoreSale(models.Model):
    product_record = models.ForeignKey(StoreProduct, on_delete=models.PROTECT)
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT)
    quantity_sold = models.IntegerField()

    def __str__(self):
        return str(self.product_record) + " " + str(self.sale.date)

class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.customer.full_name + " - " + str(self.due_date)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    blueprint = models.ForeignKey(Product, on_delete=models.PROTECT)
    builder = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    size = models.IntegerField() # in inches
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.wrist_size) + "in " + self.blueprint.name

class ItemColor(models.Model):
    slot_name = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    def __str__(self):
        return self.slot_name + ": " + self.color.name
    