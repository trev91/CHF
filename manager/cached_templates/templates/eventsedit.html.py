# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456241784.051492
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/eventsedit.html'
_template_uri = 'eventsedit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_top', 'content', 'title']


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
    return runtime._inherit_from(context, '/homepage/templates/base_app.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        action = context.get('action', UNDEFINED)
        param = context.get('param', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        all_areas = context.get('all_areas', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li><a href="/manager/events/">Events</a></li>\n  <li class="disabled"><a href="#">Edit Event</a></li>\n</ol>\n<h1 class="title text-center">\n\tEdit Event\n</h1>\n<hr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        action = context.get('action', UNDEFINED)
        all_areas = context.get('all_areas', UNDEFINED)
        param = context.get('param', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-7 text-left">\n<form method=\'POST\' action=')
        __M_writer(str(action))
        __M_writer(" id='EventsEditForm'>\n\t<table>\n  \t")
        __M_writer(str( form ))
        __M_writer('\n  </table>\n  <script type="text/javascript">\n      $(function () {\n        $(\'#id_start_date\').datetimepicker({\n               format: \'MM/DD/YYYY\'\n         });\n         $(\'#id_end_date\').datetimepicker({\n                format: \'MM/DD/YYYY\'\n          });\n          $(\'#id_add_date\').datetimepicker({\n                 format: \'MM/DD/YYYY\'\n           });\n      });\n  </script>\n\t<a href="/manager/events/" class="btn btn-danger" style="margin-left:50px; margin-top:30px">Cancel</a>\n  <button class="btn btn-primary" type="submit" style="margin-left:50px; margin-top:30px">Make Changes</button>\n</form>\n<br>\n<div class="col-md-12">\n\t<h4 class="text-center" style="margin-bottom:25px">Areas for Event</h4>\n</div>\n\n<table class="table table-striped">\n\t<tr>\n\t\t<th>Area Name:</th>\n\t\t<th>Description:</th>\n\t\t<th>Place Number:</th>\n\n\t\t<th></th>\n\t\t<th>Actions:</th>\n\t</tr>\n')
        for Area in all_areas:
            __M_writer('  <tr>\n\t\t\t<td>')
            __M_writer(str(Area.area_name))
            __M_writer('</td>\n\t\t\t<td>')
            __M_writer(str(Area.description))
            __M_writer('</td>\n      <td>')
            __M_writer(str(Area.place_number))
            __M_writer('</td>\n\n\t\t\t<td></td>\n\t\t\t<td><a id="editbutton" href="/manager/areasedit/')
            __M_writer(str(Area.id))
            __M_writer('/">Edit</a> |\n\t\t\t\t <a href="/manager/areasdelete/')
            __M_writer(str(Area.id))
            __M_writer('/" class="delete_button">Delete</a>\n  </tr>\n\t\n')
        __M_writer('\t</table>\n\t<a id="create_area_button" href="/manager/areascreate/')
        __M_writer(str(param))
        __M_writer('/" class="btn btn-sm btn-warning" style="float:right; margin-bottom:5px">New Area</a>\n\t\n\t\t<!--MODAL DELETE-->\n\t<div class="modal fade" id = "delete_modal" tabindex="-1" role="dialog">\n\t  <div class="modal-dialog" role="document">\n\t    <div class="modal-content">\n\t      <div class="modal-header">\n\t        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n\t        <h4 class="modal-title">Confirmation Requested</h4>\n\t      </div>\n\t      <div class="modal-body">\n\t        <p>Are you sure you want to delete this product?</p>\n\t      </div>\n\t      <div class="modal-footer">\n\t        <button type="button" class="btn btn-warning" data-dismiss="modal">No, Cancel</button>\n\t\t\t\t\t<!--USE JS TO GRAB THE LINK FROM THE DELETE BUTTON ABOVE-->\n\t        <a id="confirm_delete_button" href="" class="btn btn-danger">Yes, Delete</a>\n\t      </div>\n\t    </div><!-- /.modal-content -->\n\t  </div><!-- /.modal-dialog -->\n\t</div><!-- /.modal -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tEdit Venue\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/eventsedit.html", "uri": "eventsedit.html", "line_map": {"69": 6, "75": 17, "85": 17, "86": 20, "87": 20, "88": 22, "89": 22, "90": 54, "91": 55, "92": 56, "93": 56, "94": 57, "95": 57, "96": 58, "97": 58, "98": 61, "99": 61, "100": 62, "101": 62, "102": 66, "103": 67, "104": 67, "28": 0, "43": 1, "110": 3, "48": 5, "116": 3, "53": 16, "122": 116, "63": 6}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
