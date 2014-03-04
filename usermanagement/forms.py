from django import forms
from django.contrib.auth.models import User

from usermanagement.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'price', 'categories')


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number', 'email')
