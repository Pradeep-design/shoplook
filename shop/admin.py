from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Contact
from .models import Orders
from .models import OrderUpdate
from .models import Picture
from .models import SubCategoryProduct
from .models import Order_Book


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Picture)
admin.site.register(SubCategoryProduct)
admin.site.register(Order_Book)