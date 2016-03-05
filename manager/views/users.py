# MANAGER USERS.PY
from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    all_users = User.objects.order_by('last_name')
    
    template_vars = {
      'all_users': all_users,
    }
    print(all_users)
    return dmp_render_to_response(request, 'users.html', template_vars)