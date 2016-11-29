"""
(C) 2016 DeltaQuad (enwp.org/User:DeltaQuad)

This file is part of DeltaQuadBot.

DeltaQuadBot is free software: you can redistribute it and/or modify
it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DeltaQuadBot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU AFFERO GENERAL PUBLIC LICENSE for more details.

You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
along with DeltaQuadBot. If not, see <https://www.gnu.org/licenses/agpl.txt>.
"""

##Main Settings
botname = "[[User:DeltaQuadBot|DeltaQuadBot]]"

##Default System Path
winpath = "C:\\pywikipedia\\core\\"#Windows path for pywikipedia, need "\\" for folder switch
linuxpath = "/data/project/deltaquad-bots/pywikipedia/core"

#Onwiki paths
PARC = "Wikipedia:Arbitration/Requests/Case"
PARCA = "Wikipedia:Arbitration/Requests/Clarification and Amendment"
PAM = "Wikipedia:Arbitration/Requests/Motions"
##Templates
ARC = "Template:ArbComOpenTasks/CaseRequests"
OC = "Template:ArbComOpenTasks/Cases"
ARCA = "Template:ArbComOpenTasks/ClarificationAmendment"
AM = "Template:ArbComOpenTasks/Motions"
##Categories
OpenArbCaseCat = "Open ArbCom Cases"
ArbCaseCat = "Wikipedia arbitration cases"
##Bot related

#Bot Templates
ARCT = """<noinclude>
{{pp-move-indef}}
{|class="wikitable"
!Case name
!Link
!Date posted</noinclude>"""
OCT = """<noinclude>{|class="wikitable"
!Case name
!Links
!Evidence deadline
!PD deadline{{pp-semi-indef}}{{pp-move-indef}}
<!-- ADD NEW CASES TO THE BOTTOM OF THIS PAGE --></noinclude>"""
ARCAT = """<noinclude>{{pp-template|small=yes}}
{|class="wikitable"
!Request name
!Motion
!Link to case
!Date posted
<!-- PLEASE PLACE NEWER REQUESTS AT THE BOTTOM OF THIS LIST --></noinclude>"""
AMT = """<noinclude>{{pp-semi-indef}}{{pp-move-indef|small=yes}}
{|class="wikitable"
!Motion name
!Link
!Date posted
</noinclude>"""

#Runtime edit summarties
primarytaskname = botname+" "+"ArbBotClerking 0.1"
