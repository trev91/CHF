from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@view_function
def process_request(request):
  # make sure they're logged in
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/account/login/')
  # process the form
  form = ChangeAccountForm(initial={
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'address1': request.user.address1,
    'address2': request.user.address2,
  })
  if request.method == 'POST':  # just submitted the form
    form = ChangeAccountForm(request.POST)
    if form.is_valid():
      u = request.user
      u.first_name = form.cleaned_data.get('first_name')
      u.last_name = form.cleaned_data.get('last_name')
      u.address1 = form.cleaned_data.get('address1')
      u.address2 = form.cleaned_data.get('address2')
      u.save()
      #authenticate(username=u.username, password=form.cleaned_data.get('password'))
      #login(request, form.user)
      
      return HttpResponseRedirect('/homepage/index/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'myaccount.html', template_vars)
  
  
class ChangeAccountForm(forms.Form):
    
    first_name = forms.CharField(label='First Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address2 = forms.CharField(label='Address 1', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    
    def clean(self):
      pass
