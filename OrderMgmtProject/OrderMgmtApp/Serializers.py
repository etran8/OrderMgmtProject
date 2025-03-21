from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer, Address, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.customer_since = validated_data.get('customer_since', instance.customer_since)
        instance.prime_customer = validated_data.get('prime_customer', instance.prime_customer)

        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def create(self, validated_data):
        return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)

        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.order_number = validated_data.get('order_number', instance.order_number)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.order_total = validated_data.get('order_total', instance.order_total)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.account_number = validated_data.get('account_number', instance.account_number)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)

        instance.save()
        return instance


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_description = validated_data.get('item_description', instance.item_description)
        instance.item_quantity = validated_data.get('item_quantity', instance.item_quantity)

        instance.save()
        return instance


class CustomerAddressSerializer(serializers.ModelSerializer):
    contact_set = AddressSerializer()
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'prime_customer', 'customer_since', 'address_set')

    def create(self, validated_data):
        address_data = validated_data.pop('address_set')

        customer = Customer.objects.create(**validated_data)
        print(" Created Customer = ", customer.id)
        print("Address data =", address_data)
        address_serialier = self.fields['address_set']
        address_data['customer'] = customer
        address = address_serialier.create(address_data)
        # addresses = address_serializer.create(address_data)
        print(" Created Addresses = ", address.id)
        return customer

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.prime_customer = validated_data.get('prime_customer', instance.prime_customer)
        instance.customer_since = validated_data.get('customer_since', instance.customer_since)

        instance.save()
        return instance
