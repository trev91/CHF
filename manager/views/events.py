# MANAGER USERS.PY
from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from catalog.models import Event
@view_function
def process_request(request):
    all_events = Event.objects.all()


    
    
    template_vars = {
      'all_events': all_events

    }
    print(all_events)
    return dmp_render_to_response(request, 'events.html', template_vars)