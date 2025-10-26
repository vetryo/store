from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('update/<int:product_id>/<str:action>/', views.update_cart, name='update_cart'),
]
