# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454957243.351539
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
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
        __M_writer('\n\tContact Us\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t<!--This pushes the page title down so that the top nav doesn\'t cover it. -->\n\t\t\t\t\t<div class="hidden-lg hidden-md hidden-sm visible-xs-inline-block" style="padding-top:35px"></div>\n\t\t\t\t\t<!-- Comment out to remove. -->\n\t\t\t\t\t<h1 class="page-header" style="text-align:center">Contact Us</h1>\n\n\t\t\t\t</div>\n\t\t\t</div> <!-- /.row -->\n\t\t\t\t\t\n\t\t\t\t\t<div class="row">\n\t\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t\t<div class="col-md-6 pad-bottom-double">\n\t\t\t\t\t\t<div class="pad-top-none contact-intro-container">\n\t\t\t\t\t\t\t<p class="lead center-block text-center">\n\t\t\t\t\t\t\t\tPlease send us a message if you have any questions! Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t</div> <!-- /.contact-intro -->\n\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<form class="col-md-6" action ="/homepage/contact/" method="POST">\n\t\t\t\t\t\t\t\t<table>\n\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:25px">Your Name:</td>\n\t\t\t\t\t\t\t\t\t\t <td style="padding-bottom:25px"><input type="text" name="name" /></td>\n\t\t\t\t\t\t\t\t\t\t\t<tr></tr>\n\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:25px">Your Email:</td>\n\t\t\t\t\t\t\t\t\t\t\t<td style="padding-bottom:25px"><input type="text" name="email" /></td>\n\t\t\t\t\t\t\t\t\t\t\t<tr></tr>\n\t\t\t\t\t\t\t\t<td style="padding-bottom:25px">Message:</td>\n\t\t\t\t\t\t\t\t\t<td style="padding-bottom:25px"><textarea name="message"></textarea></td>\t\n\t\t\t\t\t\t\t\t\t\t\t<tr></tr>\n\t\t\t\t\t\t\t\t\t<td  style="padding-bottom:25px" colspan="2" align="center"><input type="submit" value="Send Message"/></td>\n\t\t\t\t\t\t\t\t\t<tr></tr>\n\t\t\t\t\t\t\t</table>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t</div> <!-- /.col-md-6 -->\n\t\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t</div> <!-- .row -->\n\t\t\t\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "line_map": {"64": 7, "52": 3, "37": 1, "70": 7, "76": 70, "42": 5, "28": 0, "58": 3}, "source_encoding": "utf-8", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/contact.html"}
__M_END_METADATA
"""
