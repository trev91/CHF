from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
  print('>>>> Your name was: ', request.POST.get('name'))
  print('>>>> Your email was: ', request.POST.get('email'))
  print('>>>> Your message was: ', request.POST.get('message'))
  return HttpResponseRedirect('/homepage/index/')
  template_vars = {
        'clientname': request.POST.get('name'),
        'clientemail': request.POST.get('email'),
        
  }
  print('>>>> in contact.py')
  return dmp_render_to_response(request, 'contact.html', template_vars)
  
 
