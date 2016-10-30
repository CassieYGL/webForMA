from django import forms
from web_MA_DB.models import Node,Project,Category,ProjectSheet,Userfield, Usertype
from django.contrib.auth.models import User
from django.db.models import Q

CATEGORY_CHOICES = ('1','2','3')
YEAR_CHOICES = ('2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026')
FEILD_NAMES = [(u.field_name,str(u.field_name)) for u in Userfield.objects.filter(~Q(field_id='NULL'))]
NODE_CHOICES = [(n.node_id,str(n.node_id)) for n in Node.objects.filter(~Q(node_id='NULL'))]
STATE_CHOICES = [('VIC',str('VIC')),('QLD',str('QLD')),('NSW',str('NSW')),('SA',str('SA')),('ACT',str('ACT')),
	('NZ',str('NZ')),('TAS',str('TAS')),('WA',str('WA')),('NT',str('NT')),('Overseas',str('Overseas'))]

FIELD_CHOICES = [(u.field_id,str(u.field_id)) for u in Userfield.objects.filter(~Q(field_id='NULL'))]
TYPE_CHOICES = [(u.type_id,str(u.type_id)) for u in Usertype.objects.filter(~Q(type_id='NULL'))]
INTEXT_CHOICES = [('Internal',str('Internal')),('External',str('External'))]

MONTH_CHOICES={1:('Jan'), 3:('Mar'), 4:('Apr'), 6:('Jun'), 7:('Jul'), 9:('Sep'), 10:('Oct'), 12:('Dec')}
SEARCH_CHOICES = (('Category',str('Category')),
	('UserDefined_1',str('UserDefined_1')),
	('UserDefined_2',str('UserDefined_2')),
	('State',str('State')),
	('Sum',str('Sum')))
FINANCIALYEAR = list(set([(p.pro_date.year,str(p.pro_date.year)) for p in Project.objects.all()]))


class QuarterForm(forms.Form):
	from_date =forms.DateField(label = 'From',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES, 
		months=MONTH_CHOICES))
	to_date = forms.DateField(label = 'To',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES,
		months=MONTH_CHOICES))
	
class CustomSearchForm(forms.Form):
	from_date =forms.DateField(label = 'From',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES, 
		months=MONTH_CHOICES))
	to_date = forms.DateField(label = 'To',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES,
		months=MONTH_CHOICES))	
	choices = forms.MultipleChoiceField(choices = SEARCH_CHOICES,widget=forms.CheckboxSelectMultiple)
	


class FinancialYearForm(forms.Form):
	from_date = forms.ChoiceField(label = 'From year  ', choices = FINANCIALYEAR ,required = True, widget=forms.Select())
	to_date = forms.ChoiceField(label='To  year', choices = FINANCIALYEAR, required=True,widget=forms.Select())



class ProjectForm(forms.ModelForm):
	person = forms.CharField(max_length=45, label='client contact ')
	num_sample = forms.IntegerField(min_value=0,label="number of sample ")
	pro_date = forms.DateField(label='commence date ')
	description = forms.CharField(max_length=100,label ='description ')
	service = forms.CharField(max_length=45, label='service ')
	instrument = forms.CharField(max_length=45,label='instrument ')
	organization = forms.CharField(max_length = 100,label='client organization ')
	usertype = forms.CharField(max_length=8, label = 'client type ')
	userfield = forms.CharField(max_length=15, label='project field ')
	int_ext = forms.CharField(max_length=3,label="Int/Ext UM ")
	category = forms.CharField(max_length=1,label='fund body ')
	subtotal = forms.DecimalField(min_value=0.00,max_digits=10,decimal_places=2,label="subtotal $")
	cus_count = forms.CharField(max_length=1,label='existed client ')
	class Meta:
		model = Project
		exclude = ('node','usertype','userfield','category')

# class SearchForm(forms.ModelForm):
# 	person = forms.TextInput(attrs={'required':True,'title':'Client name','size':17})
# 	num_sample = forms.IntegerField(min_value=0,label="Number of sample ",required=False)
# 	pro_date = forms.DateField(label='Commence date ',required=False)
# 	end_date = forms.DateField(label='End date ',required=False)
# 	description = forms.CharField(max_length=100,label ='Description ',required=False)
# 	service = forms.CharField(max_length=45, label='Service ',required=False)
# 	instrument = forms.CharField(max_length=45,label='Instrument ',required=False)
# 	organization = forms.CharField(max_length = 100,label='Client company ',required=False)
# 	usertype = forms.CharField(max_length=8, label = 'Client type ',required=False)
# 	userfield = forms.CharField(max_length=15, label='Project field ',required=False)
# 	int_ext = forms.CharField(max_length=3,label="Int/Ext UM ",required=False)
# 	# category = forms.CharField(max_length=1,label='fund body ')
# 	category=forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.RadioSelect,empty_label=None)

# 	class Meta:
# 		model = Project
# 		exclude = ('node','usertype','userfield',)
# 		# widgets ={'category':forms.RadioSelect(empty_label=None)}

class SearchForm(forms.Form):
	person = forms.CharField(label='Person',required=False)
	from_date = forms.DateField(label = 'From',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To',required=False,widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	organization = forms.CharField(label ='Organization',required=False)
	description = forms.CharField(label='Description',required=False)
	service = forms.CharField(label='Service',required=False)
	instrument = forms.CharField(label='Instrument',required=False)
	
class YearSearchForm(forms.Form):
	from_date = forms.IntegerField(label='From')
	to_date = forms.IntegerField(label='To')


class InvoiceSearchForm(forms.Form):
	node = forms.MultipleChoiceField(choices = NODE_CHOICES,widget=forms.CheckboxSelectMultiple)
	from_date = forms.DateField(label='From date',widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To date',widget=forms.SelectDateWidget(years = YEAR_CHOICES))


class StateSearchForm(forms.Form):
	state = forms.MultipleChoiceField(choices = STATE_CHOICES, widget=forms.CheckboxSelectMultiple)
	from_date = forms.DateField(label= "Start date",widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = "End date",widget=forms.SelectDateWidget(years = YEAR_CHOICES))


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')




class UploadFileForm(forms.Form):	
	file_name = forms.FileField(label='Select a file')
	sheet_name = forms.CharField(max_length=80,required=False,label="Selelct a sheet")
	from_row = forms.IntegerField(label="From row")
	to_row = forms.IntegerField(label="To row")


class ReconcilliationForm(forms.Form):
	from_date = forms.DateField(label='From',widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To',widget=forms.SelectDateWidget(years = YEAR_CHOICES))


class FieldForm(forms.Form):
	field = forms.MultipleChoiceField(choices = FIELD_CHOICES, widget =forms.CheckboxSelectMultiple)
	from_date = forms.DateField(label='From',widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To',widget=forms.SelectDateWidget(years = YEAR_CHOICES))



class TypeForm(forms.Form):
	usertype = forms.MultipleChoiceField(choices = TYPE_CHOICES, widget =forms.CheckboxSelectMultiple)
	from_date = forms.DateField(label='From',widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To',widget=forms.SelectDateWidget(years = YEAR_CHOICES))



class IntExtForm(forms.Form):
	intext = forms.MultipleChoiceField(choices = INTEXT_CHOICES, widget =forms.CheckboxSelectMultiple)
	from_date = forms.DateField(label='From',widget=forms.SelectDateWidget(years = YEAR_CHOICES))
	to_date = forms.DateField(label = 'To ',widget=forms.SelectDateWidget(years = YEAR_CHOICES))


class UpdateFieldForm(forms.Form):
	field_id = forms.CharField(label='Defined Abbr.')
	field_name = forms.CharField(label = 'Defined Name')
	





















