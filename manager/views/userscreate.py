from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('account.add_user', raise_exception=True)
# check django docs to re-route to different URL: like login #

def process_request(request):
  
  #process the form
  form = CreateUserForm()
  if request.method == 'POST':  # just submitted the form
    form = CreateUserForm(request.POST)
    if form.is_valid():
      u = User()
      u.username = form.cleaned_data.get('username')
      u.first_name = form.cleaned_data.get('first_name')
      u.last_name = form.cleaned_data.get('last_name')
      u.address1 = form.cleaned_data.get('address1')
      u.address2 = form.cleaned_data.get('address2')
      u.set_password(form.cleaned_data.get('password'))
      u.email = form.cleaned_data.get('email')
      u.birth = form.cleaned_data.get('birthdate')
      u.phone_number = form.cleaned_data.get('phone_number')
      
      perms = form.cleaned_data.get('user_permissions')
      groups = form.cleaned_data.get('groups')
      u.save()
      
      u.user_permissions.clear()
      for x in perms:
        u.user_permissions.add(x)
        print(x)
        
      u.groups.clear()
      for x in groups:
        u.groups.add(x)
        print(x)
      u.save()
      
     
      
      #u2 = UserUserGroups()
      
      #u2.user_id = u.id
      #u2.permission_id = form.cleaned_data.get('user_permissions')
      #u2.group = form.cleaned_data.get('groups')
      
      #u.save()
      #u2.save()
      # authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
      # login(request, form.user)    
      # create a user object
      # fill the user object with the data from the form
      return HttpResponseRedirect('/manager/users/')
      
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'userscreate.html', template_vars)
  
  
class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput())
    first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput())
    phone_number = forms.CharField(label='Phone Number', required=True, max_length=20, widget=forms.TextInput())
    email = forms.EmailField(label='Email', required=True, max_length=60, widget=forms.EmailInput())
    address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput())
    address2 = forms.CharField(label='Address 2', required=True, widget=forms.TextInput())
    birthdate = forms.DateField(label='Birth Date', required=True, widget=forms.TextInput())
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (again)', required=True, max_length=100, widget=forms.PasswordInput())
    groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=Group.objects.order_by('name'), widget=forms.CheckboxSelectMultiple())
    user_permissions = forms.ModelMultipleChoiceField(label='User Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple())
    
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
      
class CalendarWidget(forms.DateField):
  class Media:
    css = {
      'all':('/homepage/media/bootstrap3/css/bootstrap-datetimepicker.min.css',)
    }
    js = ('/homepage/media/bootstrap3/js/bootstrap-datetimepicker.min.js',)