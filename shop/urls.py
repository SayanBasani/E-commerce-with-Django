from django.urls import path,include

from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.home , name='home'),
    path('upload_item/',views.upload_item , name='upload_item'),
    path('item_review/',views.item_review , name='item_review'), 
    path('p/<str:product_id>/',views.product_Overview , name='product_Overview'), 
    path('cart/',views.cart , name='cart'), 
    path('add_to_cart/',views.add_to_cart , name='add_to_cart'), 
    path('remove_from_cart/',views.remove_from_cart , name='remove_from_cart'), 

    path('upload_sucess/',views.upload_sucess, name='upload_sucess'),
]
