from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hashlib import sha256

from usermanagement.models import Category, Item, Customer
from usermanagement.serializers import CategorySerializer, ItemSerializer, CustomerSerializer
from usermanagement.tables import *
from usermanagement.forms import *

def index(request):
	return render(request, "index.html")

@login_required
def manage(request):
	users = UserTable(User.objects.all()[:5],sortable=False)
	categories = CategoryTable(Category.objects.all()[:5],sortable=False)
	items = ItemTable(Item.objects.all()[:5],sortable=False)
	customers = CustomerTable(Customer.objects.all()[:5],sortable=False)
	context = {'users':users, 'categories':categories, 'items':items, 'customers':customers}
	return render(request, "manage.html", context)

@login_required
def add_user(request, id=None):
	if id:
		user = get_object_or_404(User, id=id)
	else:
		user = User()

	if request.method == 'POST':
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			if id:
				user.delete()
				messages.add_message(request, messages.INFO, 'Edited user successfully')
			else:
				messages.add_message(request, messages.INFO, 'Added user successfully')
			new_user = User.objects.create_user(**form.cleaned_data)
			return HttpResponseRedirect('/manage/')
		else:
			messages.add_message(request, messages.ERROR, 'Form invalid.')

	else:
		form = UserForm(instance=user)

	return render(request, "form.html", {'form':form})

@login_required
def add_edit_item(request, id=None):
	if id:
		item = get_object_or_404(Item, id=id)
	else:
		item = Item()

	if request.method == 'POST':
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Added/edited item successfully')
			return HttpResponseRedirect('/manage/item/')
	else:
		form = ItemForm(instance=item)

	return render(request, "form.html", {'form':form})

@login_required
def add_edit_customer(request, id=None):
	if id:
		customer = get_object_or_404(Customer, id=id)
	else:
		customer = Customer()

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Added/edited customer successfully')
			return HttpResponseRedirect('/manage/customer/')
	else:
		form = CustomerForm(instance=customer)

	return render(request, "form.html", {'form':form})

@login_required
def add_edit_category(request, id=None):
	if id:
		category = get_object_or_404(Category, id=id)
	else:
		category = Category()

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Added/edited category successfully')
			return HttpResponseRedirect('/manage/category/')
	else:
		form = CategoryForm(instance=category)

	return render(request, "form.html", {'form':form})

@login_required
def delete_item(request):
	if (not request.POST) or ('id' not in request.POST):
		return HttpResponse("Bad Request")
	item = get_object_or_404(Item, id=request.POST.get('id','-1'))
	item.delete()
	return HttpResponse("OK")

@login_required
def delete_customer(request):
	if (not request.POST) or ('id' not in request.POST):
		return HttpResponse("Bad Request")
	customer = get_object_or_404(Customer, id=request.POST.get('id','-1'))
	customer.delete()
	return HttpResponse("OK")

@login_required
def delete_category(request):
	if (not request.POST) or ('id' not in request.POST):
		return HttpResponse("Bad Request")
	category = get_object_or_404(Category, id=request.POST.get('id','-1'))
	category.delete()
	return HttpResponse("OK")



@login_required
def view_user(request, id=None):
	users = UserTable(User.objects.all())
	return render(request, 'viewusers.html', {'table':users})

@login_required
def view_item(request, id=None):
	items = ItemTable(Item.objects.all())
	return render(request, 'viewitems.html', {'table':items})

@login_required
def view_customer(request, id=None):
	customers = CustomerTable(Customer.objects.all())
	return render(request, 'viewcustomers.html', {'table':customers})

@login_required
def view_category(request, id=None):
	categories = CategoryTable(Category.objects.all())
	return render(request, 'viewcategories.html', {'table':categories})

@login_required
def logout_view(request):
	logout(request)
	messages.add_message(request, messages.INFO, 'Logged out successfully.')
	return HttpResponseRedirect("/")

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
