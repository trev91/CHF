from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Product
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.change_product', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  # make sure they're logged in
  # if not request.user.is_authenticated():
  # return HttpResponseRedirect('/manager/users/')
  # process the form
  param = request.urlparams[0]
  
  pr = Product.objects.get(id=param)
  
  form = ProductsEditForm(initial={
    'name': pr.name,
    'description': pr.description,
    'image': pr.image,
    'price': pr.price

    
  })
  if request.method == 'POST':  # just submitted the form
    print('YES')
    form = ProductsEditForm(request.POST)
    if form.is_valid():
      pr.name = form.cleaned_data.get('name')
      pr.description = form.cleaned_data.get('description')
      pr.image = form.cleaned_data.get('image')
      pr.price = form.cleaned_data.get('price')

      pr.save()
      
      return HttpResponseRedirect('/manager/products/')
      
  template_vars = {
    'form': form,
    'action':'/manager/productsedit/'+param+'/'
  }
  return dmp_render_to_response(request, 'productsedit.html', template_vars)
  
  
class ProductsEditForm(forms.Form):
    
    name = forms.CharField(label='Product Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    price = forms.CharField(label='Price', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    
    def clean(self):
      pass
