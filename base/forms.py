from django.forms import ModelForm
from .models import Order 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['status', 'booking_time', 'restaurant' ,'delivery_time']


class CreateUserForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email','password1' ,'password2']