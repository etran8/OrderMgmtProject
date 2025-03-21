from datetime import date

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializers import CustomerSerializer, AddressSerializer, CustomerAddressSerializer, OrderSerializer, OrderItemSerializer
from .models import Customer, Address, Order, OrderItem
from .customerForms import CustomerForm, AddressForm, AddressModelForm, CustomerModelForm

@login_required(login_url='/accounts/login/')
def index(request):
# We will retrieve all the customers from the underlying database and display them
    customers = Customer.objects.all()
    addresses = Address.objects.all()
    orders = Order.objects.all()

    paginator = Paginator(addresses, 5)  # Show 5 addresses per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html',
                  {'page_obj': page_obj, 'customers': customers, 'addresses': addresses, 'orders': orders})


def home(request):
    return HttpResponse("Hello from home view")


class AddCustomer(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.create(serializer.validated_data)
            return Response({"Success": "Customer '{}' created successfully".format(CustomerSerializer(customer).data)})


class GetCustomers(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class UpdateCustomer(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        customers = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)

    def put(self, request, id):
        customer_data = request.data
        customer = get_object_or_404(Customer.objects.all(), pk=customer_data.get('id'))
        serializer = CustomerSerializer(instance=customer, data=customer_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            customer_saved = serializer.save()
        return Response({"Success": "Customer '{}' updated successfully".format(CustomerSerializer(customer).data)})


class AddAddress(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def list(self, request, *args, **kwargs):
        cus = self.kwargs.get('id')
        self.queryset = Address.objects.all().filter(customer_id=cus)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            address = serializer.create(serializer.validated_data)
            return Response(
                {"Success": "Address '{}' created successfully".format(AddressSerializer(address).data)})


class UpdateAddress(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        accounts = Address.objects.get(id=id)
        serializer = AddressSerializer(accounts)
        return Response(serializer.data)

    def put(self, request, id):
        address_data = request.data
        address = get_object_or_404(Address.objects.all(), pk=address_data.get('id'))
        serializer = AddressSerializer(instance=address, data=address_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"Success": "Address '{}' updated successfully".format(AddressSerializer(address).data)})


class GetAddresses(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def list(self, request, *args, **kwargs):
        cus = self.kwargs.get('id')
        self.queryset = Address.objects.all().filter(customer_id=cus)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class AddOrder(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        cus = self.kwargs.get('id')
        self.queryset = Order.objects.all().filter(customer_id=cus)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.create(serializer.validated_data)
            return Response(
                {"Success": "Order '{}' created successfully".format(OrderSerializer(order).data)})


class UpdateOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        orders = Order.objects.get(id=id)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def put(self, request, id):
        order_data = request.data
        order = get_object_or_404(Order.objects.all(), pk=order_data.get('id'))
        serializer = OrderSerializer(instance=order, data=order_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
            return Response({"Success": "Order '{}' updated successfully".format(OrderSerializer(order).data)})


class GetOrders(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        cus = self.kwargs.get('id')
        self.queryset = Order.objects.all().filter(customer_id=cus)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class AddProduct(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def list(self, request, id):
        queryset = OrderItem.objects.all().filter(order_id=id)
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, id):
        serializer = OrderItemSerializer(data=request.data)
        orderitems = request.POST
        ord = id
        order = Order.objects.get(id=ord)
        order.order_total += (50.00 * int(orderitems['item_quantity']))
        order.save()

        if order.order_total >= 250.00:
            customer = Customer.objects.get(id=order.customer_id)
            customer.prime_customer = 'Y'
            customer.save()

        if serializer.is_valid(raise_exception=True):
            orderitem = serializer.create(serializer.validated_data)
            return Response({"Success": "Order Item '{}' created successfully".format(OrderItemSerializer(orderitem).data)})


class GetProducts(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemSerializer

    def list(self, request, *args, **kwargs):
        ord = self.kwargs.get('id')
        self.queryset = OrderItem.objects.all().filter(order_id=ord)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
