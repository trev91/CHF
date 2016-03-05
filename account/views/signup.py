from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

@view_function
def process_request(request):
  
  #process the form
  form = SignupForm()
  if request.method == 'POST':  # just submitted the form
    form = SignupForm(request.POST)
    if form.is_valid():
      u = User()
      u.username = form.cleaned_data.get('username')
      u.first_name = form.cleaned_data.get('first_name')
      u.last_name = form.cleaned_data.get('last_name')
      u.address1 = form.cleaned_data.get('address1')
      u.address2 = form.cleaned_data.get('address2')
      u.set_password(form.cleaned_data.get('password'))
      u.save()
      # authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
      # login(request, form.user)    
      # create a user object
      # fill the user object with the data from the form
      return HttpResponseRedirect('/homepage/index/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'signup.html', template_vars)
  
  
class SignupForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100)
    first_name = forms.CharField(label='First Name', required=True, max_length=100)
    last_name = forms.CharField(label='Last Name', required=True, max_length=100)
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (again)', required=True, max_length=100, widget=forms.PasswordInput())
    address1 = forms.CharField(label='Address 1', required=True, max_length=100)
    address2 = forms.CharField(label='Address 1', required=True)
    
    def clean_username(self):
      username = self.cleaned_data.get('username')
      # check uniqueness of the username
      # method 1- returns the user OR raises exception
      #try:
      #  user = User.objects.get(username = username)
      #  raise forms.ValidationError('This username is already taken.')
      #except User.DoesNotExist as e:
      #  pass # this is what we hope for - means username is unique
      # method 2 -
      if User.objects.filter(username=username).count() > 0:
        raise forms.ValidationError('This username is already taken.')
      return username
      
      
    def clean(self):
      if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
        raise forms.ValidationError('Your passwords do not match.')
      return self.cleaned_data