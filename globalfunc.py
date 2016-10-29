from datetime import datetime
import sys
import platform
import time
import json
import re
import traceback

import localconfig
if platform.system() == "Windows":
        sys.path.append(localconfig.winpath)
else:sys.path.append(localconfig.linuxpath)
import pywikibot
from pywikibot.data import api

useWiki = pywikibot.Site('en', 'wikipedia')

def callArbPageCollect():
    global arcpage
    arcpage = catRetrival(localconfig.OpenArbCaseCat)
    print arcpage

def callAPI(params):
    print params
    req = api.Request(site,**params)
    return req.submit()

def pageRetrival(page):
    site = pywikibot.getSite()
    pagename = page
    page = pywikibot.Page(site, pagename)
    return page.get()

def catRetrival(category):
    category = "Category:" + category
    site= pywikibot.getSite()
    params = {'action': 'query',
        	'list': 'categorymembers',
        	'cmtitle': category,
                'cmnamespace':'4',
                'cmlimit':'500',
                'format':'json',
                'rawcontinue':'1'
                }
    raw = callAPI(params)
    reg = raw["query"]["categorymembers"]
    reg = formatArray(reg)
    return reg

def formatArray(database):
    i = 0
    cases = []
    for entry in database:
        cases = cases + [entry["title"]]
    return cases

def run(start):
    callArbPageCollect()
    callTACOTProcessing(start)

def callTACOTProcessing(start):
    

    #ARC
    pageRetrival(localconfig.ARC).split("</noinclude>")[1]

    #Open
    pageRetrival(localconfig.OC).split("</noinclude>")[1]

    #ARCA
    pageRetrival(localconfig.ARCA).split("</noinclude>")[1]

    #Motions
    pageRetrival(localconfig.AM).split("</noinclude>")[1]

def ACOTGenerator(mode,name):
    line="""{{ArbComOpenTasks/line
    |mode="""+mode+"""
    |name="""+name
    if date:
        line+="""|date="""+date
    else:
        line+="{{subst:CURRENTDAY}} {{subst:CURRENTMONTHABBREV}} {{subst:CURRENTYEAR}}"
    line+="""}}"""
    return line

def processARC(text):
    #Get Current 
    try:eachcasereq = text.split("}}\n{{")
    except:return #No case requests exist on the template
    for casereq in eachcasereq:
        name = casereq.split("|name=")[1].split("\n\|")
        
    return newtext

run(True)
