from django.urls import path,include
from . import views

app_name = "account"

urlpatterns = [
  # path('',views.seller_singup , name='seller_singup'),
  path('user_singup',views.user_singup , name='user_singup'),
  path('user_login/',views.user_login , name='user_login'),
  path('seller_singup/',views.seller_singup , name='seller_singup'),
  path('seller_login/',views.seller_login , name='seller_login'),
  path('logout/',views._logout , name='logout'),
]