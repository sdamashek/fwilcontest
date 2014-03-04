from django.contrib.auth.models import User
from usermanagement.models import Item, Category, Customer
from rest_framework import serializers

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('url', 'name', 'price', 'categories')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('url', 'name')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('url', 'first_name', 'last_name', 'email', 'phone_number')
