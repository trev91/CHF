from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Venue
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.change_venue', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  # make sure they're logged in
  # if not request.user.is_authenticated():
  # return HttpResponseRedirect('/manager/users/')
  # process the form
  param = request.urlparams[0]
  
  ven = Venue.objects.get(id=param)
  
  form = VenuesEditForm(initial={
    'venue_name': ven.venue_name,
    'address1': ven.address1,
    'address2': ven.address2,
    'image': ven.image,
    'city': ven.city,
    'state': ven.state,
    'zipcode': ven.zipcode,
    

    
  })
  if request.method == 'POST':  # just submitted the form
    print('YES')
    form = VenuesEditForm(request.POST)
    if form.is_valid():
      ven.venue_name = form.cleaned_data.get('venue_name')
      ven.address1 = form.cleaned_data.get('address1')
      ven.address2 = form.cleaned_data.get('address2')
      ven.image = form.cleaned_data.get('image')
      ven.city = form.cleaned_data.get('city')
      ven.state = form.cleaned_data.get('state')
      ven.zipcode = form.cleaned_data.get('zipcode')
      
      ven.save()
      return HttpResponseRedirect('/manager/venues/')
      
  template_vars = {
    'form': form,
    'action':'/manager/venuesedit/'+param+'/'
  }
  return dmp_render_to_response(request, 'venuesedit.html', template_vars)
  
  
class VenuesEditForm(forms.Form):
    
  venue_name = forms.CharField(label='Venue Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  address2 = forms.CharField(label='Address 2', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  city = forms.CharField(label='City', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  state = forms.CharField(label='State', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  zipcode = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    
  def clean(self):
      pass
