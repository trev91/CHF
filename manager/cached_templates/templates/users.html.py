# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456000943.472308
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/users.html'
_template_uri = 'users.html'
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
        all_users = context.get('all_users', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        all_users = context.get('all_users', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li class="active"><a href="/manager/users/">Users</a></li>\n\t<li><a href="/manager/products/">Products</a></li>\n\t<li><a href="/manager/venues/">Venues</a></li>\n  <li><a href="/manager/events/">Events</a></li>\n</ol>\n<div class="col-md-12">\n\t<h2 class="text-center" style="margin-bottom:25px">User List</h2>\n</div>\n\n<table class="table table-striped">\n\t<tr>\n\t\t<th>Username:</th>\n\t\t<th>First Name:</th>\n\t\t<th>Last Name:</th>\n\t\t<th>Email:</th>\n\t\t<th>Phone Number:</th>\n\t\t<th>Birth Date:</th>\n\t\t<th></th>\n\t\t<th>Actions:</th>\n\t</tr>\n')
        for User in all_users:
            __M_writer('  <tr>\n\t\t\t<td>')
            __M_writer(str(User.username))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str(User.first_name))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str(User.last_name))
            __M_writer('</td>\n      <td>')
            __M_writer(str(User.email))
            __M_writer('</td>\n      <td>')
            __M_writer(str(User.phone_number))
            __M_writer('</td>\n      <td>')
            __M_writer(str(User.birth))
            __M_writer('</td>\n\t\t\t<td></td>\n\t\t\t<td><a href="/manager/usersedit/')
            __M_writer(str(User.id))
            __M_writer('/">Edit</a> |\n\t\t\t\t <a href="/manager/usersdelete/')
            __M_writer(str(User.id))
            __M_writer('/" class="delete_button">Delete</a>\n  </tr>\n\t\n')
        __M_writer('\t</table>\n\t\n<a id="create_user_button" href="/manager/userscreate/" class="btn btn-sm btn-warning" style="float:right; margin-bottom:5px">New User</a>\n\t\n\t<!--MODAL DELETE-->\n<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n  <div class="modal-dialog" role="document">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title">Confirmation Requested</h4>\n      </div>\n      <div class="modal-body">\n        <p>Are you sure you want to delete this user?</p>\n      </div>\n      <div class="modal-footer">\n        <button type="button" class="btn btn-warning" data-dismiss="modal">No, Cancel</button>\n\t\t\t\t<!--USE JS TO GRAB THE LINK FROM THE DELETE BUTTON ABOVE-->\n        <a id="confirm_delete_button" href="" class="btn btn-danger">Yes, Delete</a>\n      </div>\n    </div><!-- /.modal-content -->\n  </div><!-- /.modal-dialog -->\n</div><!-- /.modal -->\n\t\t\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "users.html", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/users.html", "line_map": {"64": 32, "65": 32, "66": 33, "67": 33, "68": 35, "69": 35, "70": 36, "71": 36, "72": 40, "78": 72, "28": 0, "36": 1, "46": 3, "53": 3, "54": 26, "55": 27, "56": 28, "57": 28, "58": 29, "59": 29, "60": 30, "61": 30, "62": 31, "63": 31}}
__M_END_METADATA
"""
