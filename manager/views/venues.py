# MANAGER USERS.PY
from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from catalog.models import Venue
@view_function
def process_request(request):
    all_venues = Venue.objects.all()
    
    
    template_vars = {
      'all_venues': all_venues

    }
    print(all_venues)
    return dmp_render_to_response(request, 'venues.html', template_vars)