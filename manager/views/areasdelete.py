from django_mako_plus.controller import view_function
from django.conf import settings
from .. import dmp_render, dmp_render_to_response
from django import forms
from catalog.models import Area
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required, permission_required

@view_function
@permission_required('catalog.delete_area', raise_exception=True)
# check django docs to re-route to different URL: like login #
def process_request(request):
  
  param = request.urlparams[0]
  
  a = Area.objects.get(id=param)
  a.delete()
  
  return HttpResponseRedirect('/manager/events/')
  