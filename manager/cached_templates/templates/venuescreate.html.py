# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455744494.836968
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/venuescreate.html'
_template_uri = 'venuescreate.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content_top', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_top():
            return render_content_top(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tCreate Product\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li><a href="/manager/venues/">Venues</a></li>\n  <li class="active"><a href="/manager/venuescreate/">New Venue</a></li>\n</ol>\n<h1 class="title text-center">\n\tNew Venue\n</h1>\n<hr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-7 text-left">\n<form method="POST" action="/manager/venuescreate/">\n  <table>\n      ')
        __M_writer(str( form.as_p() ))
        __M_writer('\n  </table>\n  <script type="text/javascript">\n      $(function () {\n          $(\'#id_birthdate\').datetimepicker({\n                 format: \'MM/DD/YYYY\'\n           });\n      });\n  </script>\n  <button class="btn btn-primary" type="submit" style="margin-left:30px">Create</button>\n</form>\n\n\t\t\t\t       \n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "venuescreate.html", "source_encoding": "utf-8", "line_map": {"66": 3, "99": 93, "72": 6, "28": 0, "45": 5, "78": 6, "60": 3, "40": 1, "50": 16, "84": 17, "91": 17, "92": 21, "93": 21}, "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/venuescreate.html"}
__M_END_METADATA
"""
