from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from homepage.customform import CustomForm

@view_function
def process_request(request):
  # make sure they're logged in
  if not request.user.is_authenticated():
    return HttpResponseRedirect('/account/login/')
  
  # process the form
  form = ChangePasswordForm(request)
  if request.method == 'POST':  # just submitted the form
    form = ChangePasswordForm(request.POST)
    # form.user = request.user
    if form.is_valid():
      u = request.user
      u.set_password(form.cleaned_data.get('password'))
      u.save()
      authenticate(username=u.username,password=form.cleaned_data.get('password'))
      login(request, form.user)
      return HttpResponseRedirect('/homepage/index/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'changepassword.html', template_vars)
  
  
class ChangePasswordForm(CustomForm):
  current_password = forms.CharField(label='Current password', widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
  password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
  password2 = forms.CharField(label='New Password (again)', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
    
  def clean_current_password(self):
    if not self.request.user.check_password(self.cleaned_data_get('current_password')):
      raise forms.ValidationError('Incorrect password. Try again.')
      
    return self.cleaned_data.get('current_password')
      
  def clean(self):
    if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
      raise forms.ValidationError('Your passwords do not match.')
    return self.cleaned_data
      
