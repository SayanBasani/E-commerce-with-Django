from django.contrib import admin
from .models import seller_product,item_review,ItemImage,cartItems
# Register your models here.
admin.site.register(item_review)
admin.site.register(seller_product)
admin.site.register(ItemImage)
admin.site.register(cartItems)