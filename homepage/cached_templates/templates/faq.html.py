# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453516062.216308
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/faq.html'
_template_uri = 'faq.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


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
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t<h3><span class="fa fa-pull-left fa-question-circle fa-spin fa-lg"></span>\t\tFAQs</h3>\n\t<p>Here\'s a few of our frequently asked questions.</p>\n\t\n\t<div class="container">\n\t\t<div class="col-md-12">\n\t\t\t<p><strong>\t\tWhat is so cool about CHF?</strong></p>\n\t\t\t<p>We love history! And we want you to love it too! We give you a chance to experience the past in a\n\t\t\t\tway nobody else can!</p><hr>\n\t\t\t<p><strong>Can I volunteer to be an actor?</strong></p>\n\t\t\t<p>Absolutely! Just get in touch with one of our event coordinators and we can have you acting in no time!</p>\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n\tFAQs\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "faq.html", "line_map": {"64": 3, "52": 7, "37": 1, "70": 3, "76": 70, "42": 5, "28": 0, "58": 7}, "filename": "/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/faq.html"}
__M_END_METADATA
"""
