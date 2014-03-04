import django_tables2 as tables
from usermanagement.models import *
from django.contrib.auth.models import User


class UserTable(tables.Table):
	edit = tables.TemplateColumn(template_name='edit_button.html')
	class Meta:
		model = User
		exclude=('password','first_name','last_name')
		attrs={'class':'table','id':'user'}

class CustomerTable(tables.Table):
	edit = tables.TemplateColumn(template_name='edit_button.html')
	delete = tables.TemplateColumn(template_name='delete_button.html')
	class Meta:
		model = Customer
		attrs={'class':'table','id':'customer'}

class ItemTable(tables.Table):
	categories = tables.TemplateColumn('{% load joinby from extras %} {{ record.categories.all | joinby:", " }}')
	edit = tables.TemplateColumn(template_name='edit_button.html')
	delete = tables.TemplateColumn(template_name='delete_button.html')
	class Meta:
		model = Item
		attrs={'class':'table','id':'item'}

class CategoryTable(tables.Table):
	edit = tables.TemplateColumn(template_name='edit_button.html')
	delete = tables.TemplateColumn(template_name='delete_button.html')
	class Meta:
		model = Category
		attrs={'class':'table','id':'category'}