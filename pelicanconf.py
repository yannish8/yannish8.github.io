#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

THEME = "../pelican-themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["i18n_subsites"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('About', '/pages/about.html'),
    # ('Blog', '/category/blog.html'),
    # ('Email', 'http://www.google.com/recaptcha/mailhide/d?...'),
    ('Vita', '/pdfs/yannish-resume.pdf')
    )