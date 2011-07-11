'''
Created on Jul 10, 2011

@author: ajweb.eu
'''
import datetime

from django import template
register = template.Library()

def getkey(value, arg):
    return value[arg]

def time_to_date(value):
    return datetime.datetime.fromtimestamp(value)

register.filter('getkey', getkey)
register.filter('time_to_date', time_to_date)


