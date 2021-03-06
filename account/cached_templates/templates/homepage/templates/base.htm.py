# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456298773.827926
_enable_loop = True
_template_filename = '/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_right', 'footer', 'title', 'user_message', 'content_top', 'jumbotron', 'content_center', 'main_menu', 'content', 'content_left', 'mainenance_message']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main_menu():
            return render_main_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def user_message():
            return render_user_message(context._locals(__M_locals))
        def mainenance_message():
            return render_mainenance_message(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content_top():
            return render_content_top(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n    \n')
        __M_writer('  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/scripts/base.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/scripts/moment.min.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap-datetimepicker.min.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('manager/scripts/users.js"></script>\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('manager/scripts/ajaxedit.js"></script>\n\n\t<!--script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('manager/scripts/users.js"></script-->\n\t<!-- Latest compiled and minified JavaScript -->\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\n\t<!--Font Awesome-->\n\t<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">\n\t<!--Fonts-->\n\t<link href=\'https://fonts.googleapis.com/css?family=Great+Vibes&subset=latin,latin-ext\' rel=\'stylesheet\' type=\'text/css\'>\n\t<!--Custom CSS-->\n\t<link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/styles/base.css">\n\t<link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/styles/index.css">\n\t<link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/styles/sections.css">\n\t<link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap3/css/bootstrap-datetimepicker.min.css">\n  \n')
        __M_writer('\t<link rel="stylesheet" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.css" />\n')
        __M_writer('\t<link rel="icon" type="image/png" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/favicon.ico" />\n\t\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n  \n  \n  </head>\n  <body>\n\t  <!--Padding for navbar-fixed-->\n\t  <div style="padding-top:100px"></div>\n  \n    <header>\n\t\t\n\t\t<div id="user_message">\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'user_message'):
            context['self'].user_message(**pageargs)
        

        __M_writer('\n    </header>\n\t\n\t<div id="maintenance_message">\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'mainenance_message'):
            context['self'].mainenance_message(**pageargs)
        

        __M_writer('\n\t</div>\n\t<div id="main_menu">\n  \t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main_menu'):
            context['self'].main_menu(**pageargs)
        

        __M_writer('\n\t</div>\n        \n<div id="jumbotron">\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\n</div>\n\t\n\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-12">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_top'):
            context['self'].content_top(**pageargs)
        

        __M_writer('\n\t\t\t<div class="col-md-2">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\t\t\t</div><!--left content-->\n\t\t\t<div class="col-md-8">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\n\t\t\t</div><!--center content-->\n\t\t\t<div class="col-md-2">\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n\t\t\t</div><!--right content-->\n\t\t</div>\n\t</div>\n\t\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n<footer>\n\t<div style="padding-top: 30px"></div>\n\t<hr>\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n\t<div style="padding-bottom: 30px"></div>\n</footer>\n  \n\t<!-- Latest compiled and minified JavaScript -->\n\t<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.css" ></script>\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n \n  </body>\n \n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n')
        import datetime
        current_year = datetime.date.today().year
        
        __M_writer('\n\t\t<div id="footer" class="container-fluid col-md-12">\n\t\tCopyright &copy; Trevor Hardy ')
        __M_writer(str( current_year ))
        __M_writer('\n\t\t</div>\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(' &mdash;Colonial Heritage Foundation')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def user_message():
            return render_user_message(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_top():
            return render_content_top(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main_menu():
            return render_main_menu(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n      \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\t\t\n\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mainenance_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def mainenance_message():
            return render_mainenance_message(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t\tUser is: ')
        __M_writer(str(request.user))
        __M_writer('\n\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "filename": "/Users/trevorhardy/Desktop/sec1/CHF/homepage/templates/base.htm", "line_map": {"129": 91, "178": 111, "179": 111, "134": 96, "257": 101, "209": 80, "139": 103, "269": 84, "275": 84, "144": 113, "17": 4, "146": 118, "19": 0, "148": 120, "149": 120, "281": 60, "155": 94, "197": 54, "288": 60, "161": 94, "289": 61, "251": 65, "167": 107, "296": 290, "227": 71, "263": 101, "173": 107, "174": 108, "203": 54, "49": 2, "50": 4, "51": 5, "55": 5, "290": 61, "185": 12, "221": 71, "60": 12, "61": 15, "62": 16, "63": 16, "64": 17, "65": 17, "66": 18, "67": 18, "68": 19, "69": 19, "70": 20, "71": 20, "72": 21, "73": 21, "74": 22, "75": 22, "76": 24, "77": 24, "78": 32, "79": 32, "80": 33, "81": 33, "82": 34, "83": 34, "84": 35, "85": 35, "86": 38, "87": 38, "88": 38, "89": 40, "90": 40, "91": 40, "92": 43, "93": 43, "94": 43, "99": 56, "215": 80, "145": 118, "104": 62, "233": 89, "109": 67, "177": 109, "239": 89, "114": 73, "147": 120, "245": 65, "119": 82, "191": 12, "124": 86}}
__M_END_METADATA
"""
