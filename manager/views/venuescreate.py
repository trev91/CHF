from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Venue
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required, permission_required


@view_function
@permission_required('catalog.add_venue', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  
  #process the form
  form = CreateVenueForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateVenueForm(request.POST)
    if form.is_valid():
      v = Venue()
      v.venue_name = form.cleaned_data.get('venue_name')
      v.address1 = form.cleaned_data.get('address1')
      v.address2 = form.cleaned_data.get('address2')
      v.image = form.cleaned_data.get('image')
      v.city = form.cleaned_data.get('city')
      v.state = form.cleaned_data.get('state')
      v.zipcode = form.cleaned_data.get('zipcode')

      v.save()

      return HttpResponseRedirect('/manager/venues/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'venuescreate.html', template_vars)
  
  
class CreateVenueForm(forms.Form):
    
    venue_name = forms.CharField(label='Venue Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    city = forms.CharField(label='City', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    state = forms.CharField(label='State', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    zipcode = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    
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