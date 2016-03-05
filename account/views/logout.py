from django.http import HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth import logout
from .. import dmp_render, dmp_render_to_response
from django import forms
from account.models import User
from django.http import HttpResponseRedirect




@view_function
def process_request(request):
  
 #logout the user
  logout(request)
 #redirect to the login page
  return HttpResponseRedirect('/homepage/index/')