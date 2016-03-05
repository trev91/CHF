from django.conf import settings
from django_mako_plus.controller import view_function
from django.contrib.auth import login, authenticate
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect, HttpResponse



@view_function
def process_request(request):
  
  # if already logged in, go to the account area
  if request.user.is_authenticated():
    return HttpResponseRedirect('/account/index') # or wherever your 'My Account' page is...
    # USE THIS IN NAVBAR TO SHOW LOGIN OR LOGOUT  .. If statement!
    
  
  #process the form
  form = LoginForm()
  if request.method == 'POST':  # just submitted the form
    form = LoginForm(request.POST)
    if form.is_valid():
      # log the user in
      
      login(request, form.user)
      # redirect to homepage
      return HttpResponse('''
        <script>
          window.location.href = '/homepage/index/';
        </script>
      ''')
      
  
  #show the html    
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'login.html', template_vars)
  

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control', 'style':'margin-top:20px'}))
    
    def clean(self):
      user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
      if user == None:
        raise forms.ValidationError('The username and/or password does not match our records.')
      self.user = user
      return self.cleaned_data
      
      # normal way of pulling ANY ONE model out of the database
      # user = User.objects.get(username = 'user1', password = 'something')
      # user = User.objects.get(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
      # return self.cleaned_data
      
      # we can't use what's above because the password is HASHED (Special case)
      
