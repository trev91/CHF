from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Area, Event
from catalog import models as vmod
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.add_area', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  
  param = request.urlparams[0]
  print(param + 'nothing')
  
  #process the form
  form = CreateAreaForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateAreaForm(request.POST)
    if form.is_valid():
      a = Area()
      
      a.area_name = form.cleaned_data.get('name')
      a.description = form.cleaned_data.get('description')
      a.place_number = form.cleaned_data.get('place_number')
      a.event = Event.objects.get(id=param)

      
      a.save()
      return HttpResponseRedirect('/manager/events/eventsedit/'+param+'/')

      
  template_vars = {
    'form': form,
    'action':'/manager/areascreate/'+param+'/',
    'param': param,
  }
  return dmp_render_to_response(request, 'areascreate.html', template_vars)
  
  
class CreateAreaForm(forms.Form):
    name = forms.CharField(label='Area Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    place_number = forms.CharField(label='Place Number', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  
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
      if Event.objects.filter(name=name).count() > 0:
        raise forms.ValidationError('This name is already taken.')
      return name

      
class CalendarWidget(forms.DateField):
  class Media:
    css = {
      'all':('/homepage/media/bootstrap3/css/bootstrap-datetimepicker.min.css',)
    }
    js = ('/homepage/media/bootstrap3/js/bootstrap-datetimepicker.min.js',)