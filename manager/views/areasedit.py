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
@permission_required('catalog.change_area', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  # make sure they're logged in
  # if not request.user.is_authenticated():
  # return HttpResponseRedirect('/manager/users/')
  # process the form
  
  param = request.urlparams[0]
  
  a = Area.objects.get(id=param)
  
  # filter retrieves all objects that match the filter. Get returns a single. All, returns all.
  form = AreasEditForm(initial={
    'name': a.area_name,
    'description': a.description,
    'place_number': a.place_number,
    


  })
  if request.method == 'POST':  # just submitted the form
    print('YES')
    form = AreasEditForm(request.POST)
    if form.is_valid():
      a.area_name = form.cleaned_data.get('name')
      a.description = form.cleaned_data.get('description')
      a.place_number = form.cleaned_data.get('place_number')
      
      a.save()
      return HttpResponseRedirect('/manager/events/')
      
  template_vars = {
    'form': form,
    'action':'/manager/areasedit/'+param+'/',

  }
  return dmp_render_to_response(request, 'areasedit.html', template_vars)
  
  
class AreasEditForm(forms.Form):
    
  name = forms.CharField(label='Area Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  description = forms.CharField(label='Description', required=True, max_length=2000, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
  place_number = forms.CharField(label='Place Number', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))

  
  
  pass
  
