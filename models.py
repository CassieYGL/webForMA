# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=1)
    cat_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Category'
    def __str__(self):
        return '%s' %(self.cat_id)


class Node(models.Model):
    node_id = models.CharField(primary_key=True, max_length=7)
    node_name = models.CharField(max_length=45)
    node_area = models.CharField(max_length=45)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Node'
    def __str__(self):
        return '%s' %(self.node_id)


class Organization(models.Model):
    org_id = models.CharField(primary_key=True, max_length=10)
    org_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organization'

class CatQuerySet(models.QuerySet):
    def by_cat(self,cat):
        return self.filter(category=cat)
class NodeQuerySet(models.QuerySet):
    def by_node(self,n):
        return self.filter(node=n)
class YearQuerySet(models.QuerySet):
    def by_year(self,y):
        return self.filter(pro_date__year=y)
class ServiceQuerySet(models.QuerySet):
    def by_service(self,s):
        return self.filter(service=s)
class InstrumentQuerySet(models.QuerySet):
    def by_instrument(self,i):
        return self.filter(instrument=i)
class StateQuerySet(models.QuerySet):
    def by_state(self,s):
        return self.filter(state=s)
class CountryQuerySet(models.QuerySet):
    def by_country(self,c):
        return self.filter(country=c)
class IntExtQuerySet(models.QuerySet):
    def by_intext(self,i):
        return self.filter(int_ext=i)
class UsertypeQuerySet(models.QuerySet):
    def by_usertype(self,t):
        return self.filter(usertype=t)
class UserfieldQuerySet(models.QuerySet):
    def by_userfield(self,f):
        return self.filter(userfield=f)



class Project(models.Model):
    pro_id = models.AutoField(primary_key=True)
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='node', blank=True, null=True)
    pro_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    service = models.CharField(max_length=45, blank=True, null=True)
    instrument = models.CharField(max_length=45, blank=True, null=True)
    person = models.CharField(max_length=45, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    num_sample = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    int_ext = models.CharField(max_length=3, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=11, blank=True, null=True)
    usertype = models.ForeignKey('Usertype', models.DO_NOTHING, db_column='usertype', blank=True, null=True)
    userfield = models.ForeignKey('Userfield', models.DO_NOTHING, db_column='userfield', blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_count = models.CharField(max_length=1, blank=True, null=True)
    objects = models.Manager()
    cats = CatQuerySet.as_manager()
    nodes = NodeQuerySet.as_manager()
    years = YearQuerySet.as_manager()
    svcs = ServiceQuerySet.as_manager()
    instrmts = InstrumentQuerySet.as_manager()
    states = StateQuerySet.as_manager()
    countries = CountryQuerySet.as_manager()
    intexts = IntExtQuerySet.as_manager()
    types = UsertypeQuerySet.as_manager()
    fields = UserfieldQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'Project'
    def __str__(self):
        return '%s' %(self.category)
    

class Userfield(models.Model):
    field_id = models.CharField(primary_key=True, max_length=15)
    field_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserField'


class Usertype(models.Model):
    type_id = models.CharField(primary_key=True, max_length=8)
    type_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserType'



class Invoice(models.Model):
    index_id = models.AutoField(primary_key=True)
    inv_date = models.DateField(blank=True, null=True)
    inv_no = models.CharField(max_length = 12, blank=True, null=True)
    quote_no = models.CharField(max_length=40, blank= True, null = True)
    MA_staff = models.CharField(max_length=40, blank = True, null = True)
    description = models.CharField(max_length=120, blank=True, null=True)
    service = models.CharField(max_length=45, blank=True, null=True)
    instrument = models.CharField(max_length=45, blank=True, null=True)
    person = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=800, blank=True, null=True)
    num_sample = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    int_ext = models.CharField(max_length=3, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=11, blank=True, null=True)
    usertype = models.ForeignKey('Usertype', blank=True, null=True)
    userfield = models.ForeignKey('Userfield', blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = "Invoice"


class ProjectSheet(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.FileField()
    sheet_name = models.CharField(max_length=50)

    class Meta:
        managed = False       


class InvoiceSheet(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.FileField()
    sheet_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "InvoiceSheet"

class QuoteSheet(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.FileField()
    sheet_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "QuoteSheet"


