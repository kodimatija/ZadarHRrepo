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
import xbmc,xbmcplugin,xbmcaddon,xbmcgui,sys,os,re,urllib,urllib2,xbmcvfs
from glo_var import *
from iofile import *
#######################################################################

#######################################################################
# Menu File Work Code
def processMenuFile(menuFile):
    link = openMenuFile(menuFile).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?ection="(.+?)".+?earch="(.+?)".+?ubid="(.+?)".+?laylistid="(.+?)".+?hannelid="(.+?)".+?ideoid="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    return match
#######################################################################

#######################################################################
# Adds a top level style menu item, built from menu files
def addMenuItem(name, url, mode, iconimage, fanart, description=''):
        u=sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        liz.setProperty('fanart_image', fanart)
        if mode == 50 or mode == 150 or mode == 250:
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#######################################################################

#######################################################################
# Adds a section/info line placeholder item to the menu
def addSectionItem(name, iconimage, fanart):
        u=sys.argv[0]+"?url=sectionItem&mode=100&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
#######################################################################

#######################################################################
# Adds a Search Term to the menu from a menu file
def addSearchItem(name, search_id, icon, fanart):
    work_url = "plugin://plugin.video.youtube/kodion/search/query/?q="+search_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': icon, 'banner' : os.path.join(artfolder,'banner.png'), 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a Channel to the menu from a menu file
def addChannelItem(name, channel_id, icon, fanart):
    work_url = "plugin://plugin.video.youtube/channel/"+channel_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': icon, 'banner' : os.path.join(artfolder,'banner.png'), 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a Playlist to the menu from a menu file
def addPlaylistItem(name, playlist_id, icon, fanart):
    work_url = "plugin://plugin.video.youtube/playlist/"+playlist_id+"/"
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': icon, 'banner' : os.path.join(artfolder,'banner.png'), 'fanart': fanart })
    liz.setPath(work_url)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=True)
    return ok
#######################################################################

#######################################################################
# Adds a video to the menu, populated by selecting a Playlist from a Menu
def addVideoItem(name, video_id, icon, fanart):
    work_url = "plugin://plugin.video.youtube/play/?video_id="+video_id
    ok=True
    liz=xbmcgui.ListItem(name)
    liz.setInfo( type="Video", infoLabels={ "Title": name })
    liz.setArt({ 'thumb': icon, 'banner' : os.path.join(artfolder,'banner.png'), 'fanart': fanart })
    liz.setPath(work_url)
    liz.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=work_url,listitem=liz,isFolder=False)
    return ok
#######################################################################
#######################################################################