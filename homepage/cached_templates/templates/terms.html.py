# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453435845.412827
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/terms.html'
_template_uri = 'terms.html'
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
        __M_writer('\n\tTerms\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="col-md-12" style="text-align:left">\n<h1>WEBSITE TERMS AND CONDITIONS</h1></br>\n<p>Please read these Terms of Service completely using chf.com which is owned and operated by Your Nowhere Town. This Agreement documents the legally binding terms and conditions attached to the use of the Site at chf.com.</br>\nBy using or accessing the Site in any way, viewing or browsing the Site, or adding your own content to the Site, you are agreeing to be bound by these Terms of Service. \n<h3>Intellectual Property</h3></br>\n<p>The Site and all of its original content are the sole property of Your Nowhere Town and are, as such, fully protected by the appropriate international copyright and other intellectual property rights laws.</p></br>\n<h3>Termination</h3></br>\n<p>CHF reserves the right to terminate your access to the Site, without any advance notice. </p></br>\n<h3>Changes to This Agreement</h3></br>\n<p>CHF reserves the right to modify these Terms of Service at any time. We do so by posting and drawing attention to the updated terms on the Site. Your decision to continue to visit and make use of the Site after such changes have been made constitutes your formal acceptance of the new Terms of Service.</p></br>\n<h3>Contact Us</h3></br>\n<p>If you have any questions about this Agreement, please feel free to contact us using our "Contact Us" form. </p></br>\n\n\n\t\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/terms.html", "line_map": {"64": 7, "52": 3, "37": 1, "70": 7, "76": 70, "42": 5, "28": 0, "58": 3}, "uri": "terms.html"}
__M_END_METADATA
"""
