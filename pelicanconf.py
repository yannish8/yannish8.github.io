#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yannish'
SITENAME = 'Stay Alive'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "/Users/yannish-tpm/Projects/personal/pelican-themes/resume"

# Profile information
NAME = 'Yannish Sewraz'
TAGLINE = 'Data Team Lead'
PIC = '/Users/yannish-tpm/Projects/personal/blog/content/images/yannish-india-holi.jpeg'

# sidebar links
EMAIL = 'yannish8@gmail.com'
# PHONE = '(+91) 9560038966'
# WEBSITE = 'suheb.in'
LINKEDIN = 'yannish8'
GITHUB = 'yannish8'
# TWITTER = '@iamsuheb'

CAREER_SUMMARY = 'My name is Yannish Sewraz and this is my resume. Rather than list all of the things I “can do”, ' \
                 'I decided to write, candidly, the highlights of my experiences at various stages of my professional ' \
                 'career. I did succumb to peer pressure and feel the need to write a “skills” section but everything ' \
                 'beyond that is genuine I promise. '

SKILLS = [
    {
        'title': 'PYTHON',
        'level': '70'
    },
    {
        'title': 'SQL',
        'level': '85'
    },
    {
        'title': 'EXCEL',
        'level': '95'
    },
    {
        'title': 'Javascript',
        'level': '20'
    },
    # {
    #     'title': 'PHP',
    #     'level': '85'
    # }
]

# PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '
#
# PROJECTS = [
#     {
#         'title': 'Open Source Contributions',
#         'tagline': 'Active contributor in FOSSASIA, worked on the Open Event project (both server and android '
#                    'app).Active contributor in CLTK, worked on the CLTK Web app and API.Made valuable contributions '
#                    'in phpBB, implemented a live search feature.Also made a few contributions to Processing.org and '
#                    'phpMyAdmin. '
#     },
#     {
#         'title': 'Music Hub',
#         'tagline': 'Android app that connects multiple devices via wifi and plays music in all connected devices '
#                    'simultaneously to create a loud stereo-like sound effect. '
#     },
#     {
#         'title': 'Music Timer',
#         'tagline': 'Android app that monitors phone’s movement to detect whether the user’s asleep and pause music '
#                    'playback accordingly. '
#     }
# ]

LANGUAGES = [
    {
        'name': 'French',
        'description': 'Native'
    },
    {
        'name': 'English',
        'description': 'Fluent'
    },
    {
        'name': 'Spanish',
        'description': 'Amateur'
    }
]

INTERESTS = [
    'Soccer',
    'Guitar',
    'Cooking',
    'Baking'
]

EXPERIENCES = [
    {
        'job_title': 'Data Team Lead',
        'time': 'Oct 2016 - Present',
        'company': 'WatrHub Inc., Toronto ON',
        'details': 'My mandate as Data Team Lead at WatrHub is to deliver data to clients, maintain the data in our '
                   'data warehouse and identify new data that can be added to said warehouse. Data, data, '
                   'data. I lead of team of 4 to that end. Like many management roles, my day-to-day varies wildly '
                   'but generally revolves around meeting with clients, working with my team on data projects and '
                   'writing code. '
    },
    {
        'job_title': 'Business Intelligence Analyst',
        'time': 'Sept 2017 - May 2018',
        'company': 'WatrHub Inc., Toronto ON',
        'details': 'In this role, I focused heavily on data analysis and creating visuals to help WatrHub better '
                   'understand its processes and workflows. I attempted to build a CRM to track sales, cleaned and '
                   'analyzed data in pandas and visualized it using Plotly. It was a short stint that helped me learn '
                   'a lot about Python, Jupyter, pandas and plotly. '
    },
    {
        'job_title': 'Back-End Data Analyst',
        'time': 'Feb 2017 - Sept 2017',
        'company': 'WatrHub Inc., Toronto ON',
        'details': 'This was my first role at WatrHub. I was hired as a research analyst that completed reports for '
                   'clients based on their requirements. At a high-level, my job was to conduct searches using our '
                   'internal search engine and identify promising sales opportunities for clients in the water '
                   'industry. This involved learning about a variety of technical processes, regulations, etc. in the '
                   'US water industry. '
    },
    {
        'job_title': 'Gap Year Abroad',
        'time': 'Sept 2015 - Aug 2016',
        # 'company': 'Aspiring Minds, Gurgaon IN',
        'details': 'I had what some might call a “quarter life crisis” and decided to quit my job and backpack for '
                   'indefinite amount of time which turned out to be roughly one year. It was an amazing experience '
                   'that took me to India, Thailand, Laos, Vietnam, China, Mongolia and Germany. It taught me to '
                   'value the important things in life, how to be resourceful, to persevere and much more. '
    }
]

EDUCATIONS = [
    {
        'degree': 'Bachelor of Environmental Studies',
        'meta': 'University of Waterloo',
        'time': '2008 - 2013'
    },
    {
        'degree': 'High School',
        'meta': 'École Secondaire Étienne-Brûlé',
        'time': '2008'
    }
]
