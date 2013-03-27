# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'behnam izadi <behnamizadi@yahoo.com>'
response.meta.description = 'suggestion system'
response.meta.keywords = 'proposal, suggestion, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2013'

## your http://google.com/analytics id
response.google_analytics_id = 'UA-15139566-6'

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('صفحه اصلی'), False, URL('default','index'),'')
    ]
response.menu+=[
        (SPAN('نظرات',_style='color:yellow'),False,URL('default','index'),
          [(SPAN('افزودن نظر جدید'),False,URL('default','create'),'')]
          )
                ]
#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
_()
