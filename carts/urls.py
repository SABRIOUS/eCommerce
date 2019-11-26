from django.urls import path
from .views import cart_update,cart_home

app_name = 'carts'

urlpatterns = [
    path('',cart_home,name='home'),
    path('update/',cart_update,name='update'),
]
