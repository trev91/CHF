# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456181814.359414
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/areasedit.html'
_template_uri = 'areasedit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content', 'content_top']


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
        action = context.get('action', UNDEFINED)
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
        __M_writer('\n\tEdit Area\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        action = context.get('action', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="col-md-7 text-left">\n<form method=\'POST\' action=')
        __M_writer(str(action))
        __M_writer(" id='AreasEditForm'>\n\t<table>\n  \t")
        __M_writer(str( form ))
        __M_writer('\n  </table>\n\n\t<a href="/manager/events/" class="btn btn-danger" style="margin-left:50px; margin-top:30px">Cancel</a>\n  <button class="btn btn-primary" type="submit" style="margin-left:50px; margin-top:30px">Make Changes</button>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n<ol class="breadcrumb">\n  <li><a href="/manager/index/">Admin Dashboard</a></li>\n\t<li><a href="/manager/events/">Events</a></li>\n  <li class="disabled"><a href="#">Edit Area</a></li>\n</ol>\n<h1 class="title text-center">\n\tEdit Area\n</h1>\n<hr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/areasedit.html", "uri": "areasedit.html", "source_encoding": "utf-8", "line_map": {"97": 6, "83": 20, "67": 3, "103": 97, "73": 17, "46": 5, "81": 17, "82": 20, "51": 16, "84": 22, "85": 22, "41": 1, "91": 6, "28": 0, "61": 3}}
__M_END_METADATA
"""
