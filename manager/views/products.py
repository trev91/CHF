# MANAGER USERS.PY
from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from catalog.models import Product, RentalProduct, IndividualProduct, BulkProduct

@view_function
def process_request(request):
    all_products = Product.objects.order_by('name')
    all_rental_products = RentalProduct.objects.all()
    all_individual_products = IndividualProduct.objects.all()
    all_bulk_products = BulkProduct.objects.all()
    
    template_vars = {
      'all_products': all_products,
      #'all_rental_products': all_rental_products,
      #'all_individual_products': all_individual_products,
      #'all_bulk_products': all_bulk_products,
    }
    print(all_products)
    return dmp_render_to_response(request, 'products.html', template_vars)