# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456282221.905707
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_app.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        all_products = context.get('all_products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        all_products = context.get('all_products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li><a href="/manager/users/">Users</a></li>\n\t<li class="active"><a href="/manager/products/">Products</a></li>\n\t<li><a href="/manager/venues/">Venues</a></li>\n  <li><a href="/manager/events/">Events</a></li>\n</ol>\n<div class="col-md-12">\n\t<h2 class="text-center" style="margin-bottom:25px">Product List</h2>\n</div>\n\n<table class="table table-striped">\n\t<tr>\n\t\t<th>Name:</th>\n\t\t<th>Description:</th>\n\t\t<th>Image:</th>\n\t\t<th>Price:</th>\n\t\t<th></th>\n\t\t<th>Actions:</th>\n\t</tr>\n')
        for Product in all_products:
            __M_writer('  <tr>\n\t\t\t<td>')
            __M_writer(str(Product.name))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str(Product.description))
            __M_writer('</td>\n\t\t\t<td><img src=')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/product_images/')
            __M_writer(str(Product.image))
            __M_writer('/></td>\n      <td>')
            __M_writer(str(Product.price))
            __M_writer('</td>\n\t\t\t<td></td>\n\t\t\t<td><a href="/manager/productsedit/')
            __M_writer(str(Product.id))
            __M_writer('/">Edit</a> |\n\t\t\t\t <a href="/manager/productsdelete/')
            __M_writer(str(Product.id))
            __M_writer('/" class="delete_button">Delete</a>\n  </tr>\n\t\n')
        __M_writer('\t</table>\n\t\n<a id="create_user_button" href="/manager/productscreate/" class="btn btn-sm btn-warning" style="float:right; margin-bottom:5px">New Product</a>\n\t\n\t<!--MODAL DELETE-->\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role="document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Confirmation Requested</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this product?</p>\n      </div>\n      <div class="modal-footer">\n        <button type="button" class="btn btn-warning" data-dismiss="modal">No, Cancel</button>\n\t\t\t\t<!--USE JS TO GRAB THE LINK FROM THE DELETE BUTTON ABOVE-->\n        <a id="confirm_delete_button" href="" class="btn btn-danger">Yes, Delete</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n\t\t\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/products.html", "line_map": {"64": 28, "65": 28, "66": 29, "67": 29, "68": 31, "69": 31, "70": 32, "71": 32, "72": 36, "78": 72, "28": 0, "37": 1, "47": 3, "55": 3, "56": 24, "57": 25, "58": 26, "59": 26, "60": 27, "61": 27, "62": 28, "63": 28}, "uri": "products.html"}
__M_END_METADATA
"""
