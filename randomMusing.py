#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:51:15 2017

@author: jonathanroberts
"""


import random

def random_musings():

    technique = ['D3',
             'tableau',
             'python',
             'r'
             ]

    talking_point = ['Automated Testing',
                 'AQA templates',
                 'Google Analytics',
                 'Blog Posts',
                 'user stories'
                 ]

    dash_member = ['Ross',
               'Andy',
               'Vicky',
               'Robin',
               'Karik'
                ]


    doing_phrase = ["what's happening with the",
          "have you started doing your",
        ]

    a = random.random()
    who = random.choice(dash_member)
    if a > 0.5:        
        issue = random.choice(talking_point)
        doing = random.choice(doing_phrase)
        if issue.endswith('s'):
            test = ("I've been very clear that {} are very important to me. "
                  "{}, {} {}" .format(issue, who, doing, issue) )
        else:
             test = ("I've been very clear that {} is very important to me. "
                  "{}, {} {}" .format(issue, who, doing, issue) )
    else:        
        what = random.choice(technique)
        technique.remove(what)
        option = random.choice(technique)
        dash_member.remove(who)
        expert = random.choice(dash_member)
        option = random.choice(technique)
        test = ("{} are you sure you should be using {}. {} thinks you "
              "should definitely be using {}" .format(who, what, expert, option))
    return test


