from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Event
from catalog import models as vmod
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets


@view_function
@permission_required('catalog.add_event', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  
  #process the form
  form = CreateEventForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateEventForm(request.POST)
    if form.is_valid():
      ev = Event()
      
      ev.name = form.cleaned_data.get('name')
      ev.description = form.cleaned_data.get('description')
      ev.start_date = form.cleaned_data.get('start_date')
      ev.image = form.cleaned_data.get('image')
      ev.end_date = form.cleaned_data.get('end_date')
      ev.add_date = form.cleaned_data.get('add_date')
      ev.venue = form.cleaned_data.get('venue')
      
      ev.save()
      return HttpResponseRedirect('/manager/events/')

      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'Eventscreate.html', template_vars)
  
  
class CreateEventForm(forms.Form):
    name = forms.CharField(label='Event Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    start_date = forms.DateField(label='Start Date', required=True, widget=forms.TextInput())
    end_date = forms.DateField(label='End Date', required=True, widget=forms.TextInput())
    add_date = forms.DateField(label='Date Added', required=True, widget=forms.TextInput())
    venue = forms.ModelChoiceField(label='Venue', queryset=vmod.Venue.objects.order_by('venue_name'), required=True, widget=forms.Select())
    
    
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