"""OrderMgmtProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.urls import path, include
from OrderMgmtApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index, name='home'),
    path('', RedirectView.as_view(url='/home')),
    path('AddCustomer/', views.AddCustomer.as_view(), name='add_customer_json'),
    path('GetCustomers/', views.GetCustomers.as_view(), name='get_customers_json'),
    path('UpdateCustomer/<int:id>', views.UpdateCustomer.as_view(), name='update_customer_json'),
    path('AddAddress/<int:id>', views.AddAddress.as_view(), name='add_address_json'),
    path('UpdateAddress/<int:id>', views.UpdateAddress.as_view(), name='update_address_json'),
    path('GetAddresses/<int:id>', views.GetAddresses.as_view(), name='get_addresses_json'),
    path('AddOrder/<int:id>', views.AddOrder.as_view(), name='add_order_json'),
    path('UpdateOrder/<int:id>', views.UpdateOrder.as_view(), name='update_order_json'),
    path('GetOrders/<int:id>', views.GetOrders.as_view(), name='get_orders_json'),
    path('AddProduct/<int:id>', views.AddProduct.as_view({'get': 'list', 'post': 'create'}),
         name='add_product_json'),
    path('GetProducts/<int:id>', views.GetProducts.as_view(), name='get_products_json'),
]


urlpatterns += [
    path('^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('^accounts/login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('^password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change')
]

