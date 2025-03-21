from django import forms
from django.core.exceptions import ValidationError
from django.urls import resolve
from .models import Customer, Address, Order, OrderItem
from .validators import validate_firstname, validate_lastname, validate_cell

class CustomerAddressForm(forms.Form):
    STATE_CHOICES = [
            ('SC', 'South Carolina'),
            ('NC', 'North Carolina'),
            ('GA', 'Georgia'),
            ('VA', 'Virginia'),
            ('MD', 'Maryland'),
            ('PA', 'Pennsylvania'),
            ('DE', 'Delaware'),
            ('NJ', 'New Jersey'),
            ('NY', 'New York'),
            ('CT', 'Connecticut')
    ]

    firstName = forms.CharField(max_length=25, label='Enter First Name', required=True, widget=forms.TextInput(attrs={'placeholder':'What is your Name'}))
    lastName = forms.CharField(max_length=25, label='Enter Last Name', required=True)
    message = forms.CharField(required=True, widget=forms.Textarea, label='Enter Description')
    prime_customer = forms.BooleanField(required=True, label='Select prime customer')
    state = forms.ChoiceField(required=True, label='State', choices=STATE_CHOICES)
    street = forms.CharField(required=True, label='Street name')
    city = forms.CharField(required=True, label='Enter City')
    zipcode = forms.CharField(required=True, label='Zipcode')


def __str__(self):
    return self.firstName + " - " + self.lastName


class CustomerForm(forms.Form):
    #id = forms.IntegerField(widget=forms.HiddenInput)
    PRIME_STATUS = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    current_url = ""
    firstName = forms.CharField(max_length=25, label='Enter First Name', required=True, validators=[validate_firstname])
    lastName = forms.CharField(max_length=25, label='Enter Last Name', required=True, validators=[validate_lastname])
    prime_customer = forms.ChoiceField(label='Prime Customer ', required=True, choices=PRIME_STATUS)
    customer_since = forms.DateField(label='Created Date', required=False, widget=forms.DateInput)

    def clean_preferred_customer(self):
        print("Clean Prime Customer method called")
        prime_customer = self.cleaned_data["prime_customer"]
        print("Prime Customer = " + prime_customer)
        #very important to return the data access from the cleaned_data dict
        return prime_customer


class AddressForm(forms.Form):
    STATE_CHOICES = [
        ('SC', 'South Carolina'),
        ('NC', 'North Carolina'),
        ('GA', 'Georgia'),
        ('VA', 'Virginia'),
        ('MD', 'Maryland'),
        ('PA', 'Pennsylvania'),
        ('DE', 'Delaware'),
        ('NJ', 'New Jersey'),
        ('NY', 'New York'),
        ('CT', 'Connecticut')
    ]

    street = forms.CharField(required=True, label='Enter Street name')
    city = forms.CharField(required=True, label='Enter City')
    state = forms.ChoiceField(required=True, label='State', choices=STATE_CHOICES)
    zip = forms.CharField(required=True, label='Zipcode')

class OrderForm(forms.Form):
    PAYMENT_TYPE = [
        ('C', 'Credit'),
        ('B', 'Bank'),
        ('O', 'Other')
    ]

    order_number = forms.IntegerField(required=True, label='Enter Order Number')
    order_date = forms.DateField(label='Order Date', required=False, widget=forms.DateInput)
    order_total = forms.FloatField(required=True, label='Enter Order Total')
    account_number = forms.CharField(required=True, label='Enter Street name')
    expiration_date = forms.DateField(label='Expiration Date', required=False, widget=forms.DateInput)
    payment_type = forms.ChoiceField(required=True, label='State', choices=PAYMENT_TYPE)

class AddressModelForm(forms.ModelForm):
    class Meta:
        STATE_CHOICES = [
            ('SC', 'South Carolina'),
            ('NC', 'North Carolina'),
            ('GA', 'Georgia'),
            ('VA', 'Virginia'),
            ('MD', 'Maryland'),
            ('PA', 'Philadelphia'),
            ('DE', 'Delaware'),
            ('NJ', 'New Jersey'),
            ('NY', 'New York'),
            ('CT', 'Connecticut')
        ]
        model = Address
        exclude = ("customer",)
        labels = {
            "street": "Street",
            "city": "City",
            "state": "State",
            "zip": "Zip Code",
        }
        widgets = {
            "state": forms.Select(choices=STATE_CHOICES)
        }
    def clean_state(self):
        data = self.cleaned_data["state"]
        city = self.cleaned_data['city']
        print(" Clean State method called = ", data)
        if city.lower() == "city" and "VA" not in data:
            raise ValidationError("The State should be Virginia when city is City!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class CustomerModelForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea(), max_length=4000)
    class Meta:
        CAT_CHOICES = [
            ('Y', 'Yes'),
            ('N', 'No')
        ]
        model = Customer
        fields = {"first_name", "last_name", "prime_customer", "customer_since"}
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "prime_customer": "Prime Customer",
            "customer_since": "Customer Since",
        }
        widgets = {
            "prime_customer": forms.Select(choices=CAT_CHOICES),
            "customer_since": forms.DateInput()
        }
