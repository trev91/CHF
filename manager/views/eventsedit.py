from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Event, Area
from catalog import models as vmod
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.change_event', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  # make sure they're logged in
  # if not request.user.is_authenticated():
  # return HttpResponseRedirect('/manager/users/')
  # process the form
  
  param = request.urlparams[0]
  print(param + 'nothing')
  ev = Event.objects.get(id=param)
  all_areas = Area.objects.filter(event_id=param)
  # filter retrieves all objects that match the filter. Get returns a single. All, returns all.
  form = EventsEditForm(initial={
    'name': ev.name,
    'description': ev.description,
    'start_date': ev.start_date,
    'image': ev.image,
    'end_date': ev.end_date,
    #'add_date': ev.add_date,
    'venue': ev.venue,
    


  })
  if request.method == 'POST':  # just submitted the form
    print('YES')
    form = EventsEditForm(request.POST)
    if form.is_valid():
      ev.name = form.cleaned_data.get('name')
      ev.description = form.cleaned_data.get('description')
      ev.start_date = form.cleaned_data.get('start_date')
      ev.image = form.cleaned_data.get('image')
      ev.end_date = form.cleaned_data.get('end_date')
      #ev.add_date = form.cleaned_data.get('add_date')
      ev.venue= form.cleaned_data.get('venue')
      
      ev.save()
      return HttpResponseRedirect('/manager/events/')
      
  template_vars = {
    'form': form,
    'action':'/manager/eventsedit/'+param+'/',
    'all_areas': all_areas,
    'param': param,
  }
  return dmp_render_to_response(request, 'eventsedit.html', template_vars)
  
  
class EventsEditForm(forms.Form):
    
  name = forms.CharField(label='Event Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  start_date = forms.DateField(label='Start Date', required=True, widget=forms.TextInput())
  end_date = forms.DateField(label='End Date', required=True, widget=forms.TextInput())
  #add_date = forms.DateField(label='Date Added', required=True, widget=forms.TextInput())
  venue = forms.ModelChoiceField(label='Venue', queryset=vmod.Venue.objects.order_by('venue_name'), required=True, widget=forms.Select())
 # venue = forms.ModelChoiceField(label='Venue', queryset=vmod.Venue.objects.values('venue_name').order_by('venue_name'), required=True, widget=forms.Select())
  
  
  pass
  
