from datetime import datetime import sys import platform import time
import json import re import traceback

import localconfig
if platform.system() == "Windows":
        sys.path.append(localconfig.winpath)
else:sys.path.append(localconfig.linuxpath)
import pywikibot
from pywikibot.data import api

useWiki = pywikibot.Site('en', 'wikipedia')

def callArbPageCollect():
    global opencase
    opencase = catRetrival(localconfig.OpenArbCaseCat,"Template")
    return

def callArbCaseRequests():
    global arcrequests
    arcpage = pageRetrival(localconfig.PARC)
    arcrequests = getHeaders(arcpage)
    return

def callARCA():
    removed = ""
    tacot = pageRetrival(localconfig.ARCA)
    global arcarequests
    arcarequests = ""
    arcapage = pageRetrival(localconfig.PARCA)
    #Get level 2
    arcaleveltwo = getHeaders(arcapage)
    #Check removed ARCAs         
    tacotline = tacot.split("|name=")
    for line in tacotline:
            name = line.split("\n|")
            if name not in tacot:
                    continue
            else:
                    removed += name
    #Check if preexist
    for arcaline in arcaleveltwo:
            if acraline in removed or acraline in tacot:
                    continue
            else:
                    name = acraline.split(": ")[1]
                    if acraline.split(": ")[0] == "Amendment":mode = "amendment"
                    if acraline.split(": ")[0] == "Clarification":mode = "clarification"
                    if checkCat(name):link = name
                    else:link = ""
                    arcarequests += ACOTGenerator(mode,name,link)+ "\n"
                    
    return
def checkCat(name):
        cat = catRetrival(localconfig.ArbCaseCat)
        for entry in cat:
                if "Wikipedia:Requests for arbitration/" in entry:entry=entry.split("Wikipedia:Requests for arbitration/")[1]
                if "Wikipedia:Arbitration/Requests/Case/" in entry:entry=entry.split("Wikipedia:Arbitration/Requests/Case/")[1]
                if entry == name:return True
        return False
def getHeaders(text):
    return re.findall("^==([A-Za-z0-9]*| *)==",text,re.M) + (re.findall("^== ([A-Za-z0-9]*) ==",text,re.M)
                    

def callAPI(params):
    req = api.Request(useWiki,**params)
    return req.submit()

def pageRetrival(page):
    site = pywikibot.getSite()
    pagename = page
    page = pywikibot.Page(site, pagename)
    return page.get()

def catRetrival(category,skip=None):
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
    reg = formatArray(reg,skip)
    return reg

def formatArray(database,skip):
    cases = []
    for entry in database:
        if skip in entry:
                cases = cases + [entry["title"]]
    return cases

def run(start):
    ################################
    ##                            ##
    ##     Main program run       ##
    ##                            ##
    ################################
    callArbCaseRequests()
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

def ACOTGenerator(mode,name,link=None):
    line="""{{ArbComOpenTasks/line
    |mode="""+mode+"""
    |name="""+name
    if link != None:
        line+="""|date="""+link
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
