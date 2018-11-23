#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Kids Nation
# Addon id: plugin.video.kidsnation
# Addon Provider: MuadDib

#######################################################################
#Import Modules Section
import urllib, urllib2, re, xbmcplugin, xbmcgui, os, sys, datetime
from resources.lib.glo_var import *
from resources.lib.menu import *
from resources.lib.tools import *
#######################################################################

###################################################################################
# Categories/Default Menu
def Main_Menu():
    addMenuItem('[COLOR springgreen][B]News and Updates[/B][/COLOR]', 'popup', 101, DEFAULTICON, DEFAULTFANART)
    addMenuItem('[COLOR snow][B]Tools[/B][/COLOR]', 'tools', 150, DEFAULTICON, DEFAULTFANART)
    addSectionItem(' ', DEFAULTBLANK, DEFAULTFANART)

    menuItems = processMenuFile(MAINMENUFILE)
    for name,section,searchid,subid,playlistid,channelid,videoid,iconimage,fanart,description in menuItems:
        if not subid == 'false': # Means this item points to a submenu
            url = subid
            addMenuItem(name, url, 50, iconimage, fanart, description)
        elif not searchid == 'false': # Means this is a search term
            addSearchItem(name, searchid, iconimage, fanart)
        elif not videoid == 'false': # Means this is a video id entry
            addVideoItem(name, videoid, iconimage, fanart)
        elif not channelid == 'false': # Means this is a channel id entry
            addChannelItem(name, channelid, iconimage, fanart)
        elif not playlistid == 'false': # Means this is a playlist id entry
            addPlaylistItem(name, playlistid, iconimage, fanart)
        elif not section == 'false': # Means this is a section placeholder/info line
            addSectionItem(name, DEFAULTBLANK, DEFAULTFANART)
        xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
# Sub Menu
def Sub_Menu(subid):
    thisMenuFile = BASEURL + subid + '.txt'
    menuItems = processMenuFile(thisMenuFile)
    for name,section,searchid,subid,playlistid,channelid,videoid,iconimage,fanart,description in menuItems:
        if not subid == 'false': # Means this item points to a submenu
            url = subid
            addMenuItem(name, url, 50, iconimage, fanart, description)
        elif not searchid == 'false': # Means this is a search term
            addSearchItem(name, searchid, iconimage, fanart)
        elif not videoid == 'false': # Means this is a video id entry
            addVideoItem(name, videoid, iconimage, fanart)
        elif not channelid == 'false': # Means this is a channel id entry
            addChannelItem(name, channelid, iconimage, fanart)
        elif not playlistid == 'false': # Means this is a playlist id entry
            addPlaylistItem(name, playlistid, iconimage, fanart)
        elif not section == 'false': # Means this is a section placeholder/info line
            addSectionItem(name, DEFAULTBLANK, DEFAULTFANART)
        xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

###################################################################################
# Tools Menu
def Tools_Menu():
    addMenuItem('Apply ' + ADDONTITLE + ' API to YouTube (Daily Limit Fix)', 'dailylimit', 151, DEFAULTICON, DEFAULTFANART)
    addSectionItem(' ', DEFAULTBLANK, DEFAULTFANART)
    xbmc.executebuiltin('Container.SetViewMode(50)')
###################################################################################

#######################################################################
# News and Update Code
def Update_News():
        message=open_news_url(NEWSFILE)
        localnewsfile = os.path.join(KNADDONPATH, 'whatsnew.txt')
        r = open(localnewsfile)
        compfile = r.read()       
        if len(message)>1:
                if compfile == message:pass
                else:
                        text_file = open(localnewsfile, "w")
                        text_file.write(message)
                        text_file.close()
                        compfile = message
        showText('[B][COLOR springgreen]Latest Updates and Information[/COLOR][/B]', compfile)
        
def open_news_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'klopp')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        print link
        return link

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except: pass
#######################################################################

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]

        return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
    try:
        mode=params["mode"]
    except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: token=0
try: page=int(params["page"])
except: page = 1

if mode==None or url==None or len(url)<1:
        Main_Menu() # Duh
elif mode==50:
        Sub_Menu(url) # Derka
elif mode==100:
        pass # Placeholder, no action as this is for "Section" or "Info Text" used in menu lines
elif mode==101:
        Update_News() # In today's news, an increase in sandworm attacks
elif mode==150:
        Tools_Menu() # Load Tools Menu
elif mode==151:
        Apply_API() # Apply Custom API To YouTube for this Addon
xbmcplugin.endOfDirectory(int(sys.argv[1]))
