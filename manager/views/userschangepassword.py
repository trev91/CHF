from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from homepage.customform import CustomForm
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
  try:
      User.objects.get(id=request.urlparams[0])
  except User.DoesNotExist:
    return HttpResponseRedirect('/manager/users/')
  
  
  

  form = ChangePasswordForm(request)
  
  if request.method == 'POST':  # just submitted the form
    form = ChangePasswordForm(request, request.POST)
    u = User.objects.get(id=param)
   
    if form.is_valid():
      
      u.set_password(form.cleaned_data.get('password'))
      u.save()
      
      return HttpResponseRedirect('/manager/users/')
      
  template_vars = {
    'form': form,
    'toPW1': param+'/'
    
  }
  return dmp_render_to_response(request, 'userschangepassword.html', template_vars)
  
  
class ChangePasswordForm(CustomForm):
  password = forms.CharField(label='New Password', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
  password2 = forms.CharField(label='New Password (again)', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))

  #def clean_current_password(self):
  #  if not self.request.user.check_password(self.cleaned_data_get('current_password')):
  #    raise forms.ValidationError('Incorrect password. Try again.')
  
  #  return self.cleaned_data.get('current_password')
  
  def clean(self):
    if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
      raise forms.ValidationError('Your passwords do not match.')
    return self.cleaned_data
  
  