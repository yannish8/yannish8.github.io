#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = "Yannish"
SITENAME = "Stay Alive"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Toronto"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# MARKUP = ("md", "ipynb")

THEME = "pelican-themes/pelican-bootstrap3"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["i18n_subsites"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

GOOGLE_ANALYTICS = "UA-92608904-1"

EXTRA_HEADER = open('_nb_header.html').read() if os.path.exists('_nb_header.html') else None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Resume', '/pdfs/yannish-resume.pdf')
    )

ABOUT_ME = "My name is Yannish. This is my blog. Hope you find something useful within it!"
AVATAR = "images/yannish-india-holi.png"
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/yannish8/'),
          ('github', 'https://github.com/yannish8'))

STATIC_PATHS = ['images', 'pdfs']