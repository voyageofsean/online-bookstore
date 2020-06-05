from django.contrib import admin
from .models import Book,User,ShoppingCart,Order
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(ShoppingCart)
admin.site.register(Order)