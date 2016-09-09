# -*- coding: UTF-8 -*-

"""
 Copyright (c) 2016, TP-Link Co.,Ltd.
 Author:  tanghuifeng <tanghuifeng@tp-link.net>
 Created: 2016/9/9
"""

from django.forms.widgets import Select, SelectMultiple
from django.utils.safestring import mark_safe
import uuid

try:
    import json
except ImportError:
    from django.utils import simplejson as json
try:
    from django.utils.encoding import force_unicode as force_text
except ImportError:  # python3
    from django.utils.encoding import force_text

__all__ = ('Selectator', 'SelectatorMultiple')

selectator_options = {
    'prefix': 'selectator_',  # CSS class prefix
    'height': 'auto',  # auto or element
    'useDimmer': False,  # dims the screen when option list is visible
    'useSearch': True,  # if false, the search boxes are removed and
    #   `showAllOptionsOnFocus` is forced to true
    'keepOpen': False,  # if true, then the dropdown will not close when
    #   selecting options, but stay open until losing focus
    'showAllOptionsOnFocus': True,  # shows all options if input box is empty
    'selectFirstOptionOnSearch': True,  # selects the topmost option on every search
    # 'searchCallback': '', # Callback function when enter is pressed and
    'labels': {
        'search': 'Search...'  # Placeholder text in search box in single select box
    },
}

js_template = '''
    <script>
        (function(window) {
            var callback = function() {
                $(function(){$("#%(selectator_id)s").selectator(%(options)s);});
            };
            if(window.addEventListener)
                window.addEventListener("load", callback, false);
            else if (window.attachEvent)
                window.attachEvent("onload", callback);
            else window.onload = callback;
        })(window);
    </script>'''


class GMedia(object):
    js = ['project_manager/lib/jquery/jquery-2.1.3.min.js',
          'project_manager/lib/selectator/fm.selectator.jquery.js',
          ]
    css = {'all': ('project_manager/lib/selectator/fm.selectator.jquery.css',), }


class Selectator(Select):
    class Media(object):
        js = GMedia.js
        css = GMedia.css

    def __init__(self, attrs=None, choices=(), options=selectator_options):
        super(Selectator, self).__init__(attrs=attrs, choices=choices)
        self.options = options

    def render(self, name, value, attrs=None, choices=()):
        if attrs is None:
            attrs = {}
        if 'id' not in attrs:
            attrs.update({'id': uuid.uuid1()})
        dom_id = attrs['id']
        html = super(Selectator, self).render(name, value, attrs=attrs)
        js = js_template % dict(
            selectator_id=dom_id,
            options=json.dumps(self.options),
        )
        return mark_safe(force_text(html + js))


class SelectatorMultiple(SelectMultiple):
    class Media(object):
        js = GMedia.js
        css = GMedia.css

    def __init__(self, attrs=None, choices=(), options=selectator_options):
        super(SelectatorMultiple, self).__init__(attrs=attrs, choices=choices)
        self.options = options

    def render(self, name, value, attrs=None, choices=()):
        print(value)
        if attrs is None:
            attrs = {}
        if 'id' not in attrs:
            attrs.update({'id': uuid.uuid1()})
        dom_id = attrs['id']

        html = super(SelectatorMultiple, self).render(name, value, attrs=attrs)
        js = js_template % dict(
            selectator_id=dom_id,
            options=json.dumps(self.options),
        )
        return mark_safe(force_text(html + js))
