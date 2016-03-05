from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Product
from account import models as amod
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.add_product', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  
  #process the form
  form = CreateProductForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateProductForm(request.POST)
    if form.is_valid():
      pr = Product()
      pr.name = form.cleaned_data.get('name')
      pr.description = form.cleaned_data.get('description')
      pr.image = form.cleaned_data.get('image')
      pr.price = form.cleaned_data.get('price')
      pr.ptype = form.cleaned_data.get('ptype')
      pr.creator = form.cleaned_data.get('creator')
      pr.quantity = form.cleaned_data.get('quantity')
      pr.status = form.cleaned_data.get('status')
      pr.date_made = form.cleaned_data.get('date_made')

      pr.save()

      return HttpResponseRedirect('/manager/products/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'productscreate.html', template_vars)

RENTAL_STATUS_CHOICES = (
  ('current', 'Rentable'),
  ('damaged', 'Damaged'),
  ('retired', 'No Longer Rentable'),
)  
PRODUCT_TYPE_CHOICES = (
  ('',''),
  ('RentalProduct', 'Rental Product'),
  ('IndividualProduct', 'Individual Product'),
  ('BulkProduct', 'Bulk Product'),
)
  
class CreateProductForm(forms.Form):
    name = forms.CharField(label='Product Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    price = forms.CharField(label='Price', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    ptype = forms.ChoiceField(label="Product Type", required=True, choices=PRODUCT_TYPE_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.order_by('last_name','first_name'), widget=forms.Select())
    quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    status = forms.ChoiceField(label='Rental Status', required=False, choices=RENTAL_STATUS_CHOICES, widget=forms.Select(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    date_made =  forms.DateField(label='Date Made', required=True, widget=forms.TextInput())
    def clean_username(self):
      name = self.cleaned_data.get('name')
      # check uniqueness of the username
      # method 1- returns the user OR raises exception
      #try:
      #  user = User.objects.get(username = username)
      #  raise forms.ValidationError('This username is already taken.')
      #except User.DoesNotExist as e:
      #  pass # this is what we hope for - means username is unique
      # method 2 -
      if Product.objects.filter(name=name).count() > 0:
        raise forms.ValidationError('This name is already taken.')
      return name

      
class CalendarWidget(forms.DateField):
  class Media:
    css = {
      'all':('/homepage/media/bootstrap3/css/bootstrap-datetimepicker.min.css',)
    }
    js = ('/homepage/media/bootstrap3/js/bootstrap-datetimepicker.min.js',)