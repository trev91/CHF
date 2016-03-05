# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455808745.418963
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n\t<div class="col-md-6">\n\t\t<h2>Admin Dashboard</h2>\n\t\t<hr>\n\t</div>\n</div>\n<div class="row">\n\t<div class="col-md-3">\n\t\t<div class="thumbnail">\n\t\t\t<a href="/manager/users/">\n\t\t\t<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/manager/media/users.png" alt="...">\n\t\t\t<div class="caption">\n\t\t\t\t<h3 class="text-center">Users</h3>\n\t\t\t</div>\n\t\t</a>\n\t  </div>\n\t</div>\n\t<div class="col-md-3">\n\t\t<div class="thumbnail">\n\t\t\t<a href="/manager/products/">\n\t\t\t<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/manager/media/shoppingbag.png" alt="...">\n\t\t\t<div class="caption">\n\t\t\t\t<h3 class="text-center">Products</h3>\n\t\t\t</div>\n\t\t</a>\n\t  </div>\n\t</div>\n\t<div class="col-md-3">\n\t\t<div class="thumbnail">\n\t\t\t<a href="/manager/venues/">\n\t\t\t<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/manager/media/location.png" alt="...">\n\t\t\t<div class="caption">\n\t\t\t\t<h3 class="text-center">Venues</h3>\n\t\t\t</div>\n\t\t</a>\n\t  </div>\n\t</div>\n\t<div class="col-md-3">\n\t\t<div class="thumbnail">\n\t\t\t<a href="/manager/events/">\n\t\t\t<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('/manager/media/events.png" alt="..." class="img-circle">\n\t\t\t<div class="caption">\n\t\t\t\t<h3 class="text-center">Events</h3>\n\t\t\t</div>\n\t\t</a>\n\t  </div>\n\t</div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "line_map": {"67": 61, "36": 1, "60": 44, "46": 3, "53": 3, "54": 14, "55": 14, "56": 24, "57": 24, "58": 34, "59": 34, "28": 0, "61": 44}, "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/index.html"}
__M_END_METADATA
"""
