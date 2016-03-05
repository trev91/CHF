# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456337541.026046
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/productsedit.html'
_template_uri = 'productsedit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_top', 'title', 'content']


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
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        action = context.get('action', UNDEFINED)
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
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li><a href="/manager/products/">Products</a></li>\n  <li class="disabled"><a href="#">Edit Product</a></li>\n</ol>\n<h1 class="title text-center">\n\tEdit Product\n</h1>\n<hr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tEdit Product\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        action = context.get('action', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-7 text-left">\n<form method=\'POST\' action=')
        __M_writer(str(action))
        __M_writer(" id='ProductsEditForm'>\n\t<table>\n  \t")
        __M_writer(str( form ))
        __M_writer('\n  </table>\n  <script type="text/javascript">\n      $(function () {\n          $(\'#id_birthdate\').datetimepicker({\n                 format: \'MM/DD/YYYY\'\n           });\n      });\n  </script>\n\t<a href="/manager/products/" class="btn btn-danger" style="margin-left:50px; margin-top:30px">Cancel</a>\n  <button class="btn btn-primary" type="submit" style="margin-left:50px; margin-top:30px">Make Changes</button>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/productsedit.html", "uri": "productsedit.html", "line_map": {"96": 22, "97": 22, "67": 6, "103": 97, "73": 3, "46": 5, "61": 6, "51": 16, "85": 17, "41": 1, "79": 3, "28": 0, "93": 17, "94": 20, "95": 20}}
__M_END_METADATA
"""
