from django.urls import path
from . import views

urlpatterns = [
     path('', views.cart_inventory,name='cart_inventory' ),
     path('add/', views.cart_add,name='cart_add'),
     path('update_qty/', views.cart_update_qty,name='cart_update_qty'),
     path('update_status/', views.cart_update_status,name='cart_update_status'),
     path('delete/', views.cart_delete,name='cart_delete'),
     path('create_order', views.create_order, name='create_order'),
     path('add_address', views.add_address, name='add_address'),
     path('update_profile', views.update_profile, name='update_profile'),
     path('update_address/<int:addid>' , views.update_address, name='update_address'),
     path('order_detail/<int:order_id>' , views.order_detail, name='order_detail'),
     path('order_cancel/<int:order_id>' , views.order_cancel, name='order_cancel'),
    # path('update/', views.cart_update,name='cart_update'),
]