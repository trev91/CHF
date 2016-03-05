from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('account.change_user', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  # make sure they're logged in
  # if not request.user.is_authenticated():
  # return HttpResponseRedirect('/manager/users/')
  # process the form
  param = request.urlparams[0]
  
  u = User.objects.get(id=param)
  
  form = UsersEditForm(initial={
    
    'first_name': u.first_name,
    'last_name': u.last_name,
    'address1': u.address1,
    'address2': u.address2,
    'birthdate': u.birth,
    'email': u.email
    
  })
  if request.method == 'POST':  # just submitted the form
    form = UsersEditForm(request.POST)
    if form.is_valid():
      u.first_name = form.cleaned_data.get('first_name')
      u.last_name = form.cleaned_data.get('last_name')
      u.address1 = form.cleaned_data.get('address1')
      u.address2 = form.cleaned_data.get('address2')
      u.email = form.cleaned_data.get('email')
      u.birth = form.cleaned_data.get('birthdate')
      u.phone_number = form.cleaned_data.get('phone_number')
      u.save()
      #authenticate(username=u.username, password=form.cleaned_data.get('password'))
      #login(request, form.user)
      
      return HttpResponseRedirect('/manager/users/')
      
  template_vars = {
    'form': form,
    'action':'/manager/usersedit/'+param+'/',
    'toPW':param+'/'
  }
  return dmp_render_to_response(request, 'usersedit.html', template_vars)
  
  
class UsersEditForm(forms.Form):
    
    first_name = forms.CharField(label='First Name', required=True, max_length=100,widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    address2 = forms.CharField(label='Address 1', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    email = forms.EmailField(label='Email', required=True, max_length=60, widget=forms.EmailInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    birthdate = forms.DateField(label='Birth Date', required=True,  widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    phone_number = forms.CharField(label='Phone Number', required=True, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-left:20px'}))
    
    def clean(self):
      pass
