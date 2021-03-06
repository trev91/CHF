# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456242415.312587
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/base_app.htm'
_template_uri = 'base_app.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'main_menu', 'content']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\t\t\n\t\t\n')
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
        __M_writer('Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def main_menu():
            return render_main_menu(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\t\t<nav class="navbar navbar-default navbar-fixed-top">\n\t\t  <div class="container-fluid">\n\t\t    <!-- Brand and toggle get grouped for better mobile display -->\n\t\t    <div class="navbar-header">\n\t\t      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n\t\t        <span class="sr-only">Toggle navigation</span>\n\t\t        <span class="icon-bar"></span>\n\t\t        <span class="icon-bar"></span>\n\t\t        <span class="icon-bar"></span>\n\t\t      </button>\n\t\t      <a class="navbar-brand" style="shadowed" href="/"><span style="font-family: Great Vibes"><span style="color:#FF6863"><span style="font-size:1.5em">Colonial Heritage Foundation</span></span></span><!--<img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/chftransparent.png">--></a>\n\t\t    </div>\n\n\t\t    <!-- Collect the nav links, forms, and other content for toggling -->\n\t\t    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n\t\t      <ul class="nav navbar-nav" style="padding-left:50px">\n\t\t        <li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'users' else ''))
        __M_writer('"><a href="/manager/users/"><span style="color:white">Users</span></a></li>\n\t\t       \n\t\t\t\t\t\t<li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'products' else ''))
        __M_writer('"><a href="/manager/products/"><span style="color:white">Products</span></a></li>\n\t\t\t\t\t\t<li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'venues' else ''))
        __M_writer('"><a href="/manager/venues/"><span style="color:white">Venues</span></a></li>\n\t\t\t\t\t\t<li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'events' else ''))
        __M_writer('"><a href="/manager/events/"><span style="color:white">Events</span></a></li>\n\t\t\t\t\t\t<li class="')
        __M_writer(str( 'active' if request.dmp_router_page == 'index' else ''))
        __M_writer('"><a href="/homepage/index/"><span style="color:white">Home</span></a></li>\n\t\t      \n\n\n')
        if request.user.is_authenticated():
            __M_writer('<!--HTML for dropdown and logout and my account -->\n\t\t\t\t\t<div class="dropdown nav navbar-nav navbar-right push-right dropdown-menu-right">\n  \t\t\t\t\t<li class="dropdown-toggle dropdown-menu-right push-right" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"><a href="#"><span style="color:white">My Account<span class="caret"></span></span></a>\n  \t\t\t\t\t</li>\n  \t\t\t\t\t<ul class="dropdown-menu" aria-labelledby="dropdownMenu1">\n    \t\t\t\t\t<li class="')
            __M_writer(str( 'active' if request.dmp_router_page == 'myaccount' else ''))
            __M_writer('"><a href="/account/myaccount/"><span style="color:white">My Account Information</span></a></li>\n    \t\t\t\t\t<li id="logoutbutton"><a href="/account/logout/"><span style="color:white">Logout</span></a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\n\n\t\t\t  </ul>\n\t\t    </div><!-- /.navbar-collapse -->\n\t\t  </div><!-- /.container-fluid -->\n\t\t</nav>\n')
        else:
            __M_writer('<!-- Login link -->\n\t\t\t  <ul class="nav navbar-nav navbar-right">\n\t\t\t    <li id="loginbutton" class="')
            __M_writer(str( 'active' if request.dmp_router_page == 'Login' else ''))
            __M_writer('"><a href="#"><span style="color:white">Login</span></a>\n\t\t\t\t\t</li>\n\t\t\t    <li class="')
            __M_writer(str( 'active' if request.dmp_router_page == 'Signup' else ''))
            __M_writer('" style="padding-right:30px"><a href="/account/signup/"><span style="color:white">Signup</span></a>\n\t\t\t\t\t</li>\n\t\t\t  </ul>\n\t\t    </div><!-- /.navbar-collapse -->\n\t\t  </div><!-- /.container-fluid -->\n\t\t</nav>\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base_app.htm", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/manager/templates/base_app.htm", "line_map": {"67": 3, "73": 5, "28": 0, "81": 5, "82": 16, "83": 16, "84": 22, "85": 22, "86": 24, "87": 24, "88": 25, "89": 25, "90": 26, "91": 26, "92": 27, "93": 27, "94": 31, "95": 32, "96": 37, "97": 37, "98": 47, "99": 48, "100": 50, "101": 50, "102": 52, "103": 52, "104": 59, "41": 1, "110": 63, "46": 3, "51": 61, "116": 63, "122": 116, "61": 3}}
__M_END_METADATA
"""
