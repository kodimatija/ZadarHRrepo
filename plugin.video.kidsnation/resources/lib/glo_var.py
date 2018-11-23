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
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import xbmcvfs
import base64
import os
import sys
#######################################################################

#######################################################################
# Primary Addon Variables 
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
THISADDON           = xbmcaddon.Addon(id=AddonID)
ADDON_ID            = xbmcaddon.Addon().getAddonInfo('id')
URL                 = base64.b64decode(b'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL211YWRkaWJ0dHYva2lkc25hdGlvbi9tYXN0ZXIv')
ADDONTITLE          = base64.b64decode(b'S2lkcyBOYXRpb24=')
USER_AGENT          = base64.b64decode(b'VGFudHJ1bUFkZG9uQWdlbnQ=')
#######################################################################

#######################################################################
# Path Variables
HOMEPATH            = xbmc.translatePath('special://home/')
ADDONSPATH          = os.path.join(HOMEPATH, 'addons')
USERDATAPATH        = os.path.join(HOMEPATH, 'userdata')
ADDONDATAPATH       = xbmc.translatePath(os.path.join(USERDATAPATH, 'addon_data'))
LOGPATH             = xbmc.translatePath('special://logpath/')
KNADDONPATH         = os.path.join(ADDONSPATH, ADDON_ID)
KNDATAPATH          = os.path.join(ADDONDATAPATH, ADDON_ID)
YTADDONPATH         = os.path.join(ADDONSPATH, 'plugin.video.youtube')
YTADDONDATAPATH     = os.path.join(ADDONDATAPATH, 'plugin.video.youtube')
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = URL
MAINMENUFILE        = BASEURL + base64.b64decode(b'a25tYWluLnR4dA==')
NEWSFILE            = BASEURL + base64.b64decode(b'bmV3cy54bWw=')
#######################################################################

#######################################################################
# Artwork Variables 
DEFAULTICON         = os.path.join(KNADDONPATH, 'icon.png')
DEFAULTFANART       = os.path.join(KNADDONPATH, 'fanart.jpg')
DEFAULTBLANK        = os.path.join(KNADDONPATH, 'resources/art/pixel.png')
#######################################################################

#######################################################################
# Settings Variables 
DEBUGMODE           = THISADDON.getSetting('debug')
#######################################################################

artfolder           = os.path.join(KNADDONPATH,'resources','img')

def translate(text):
    return THISADDON.getLocalizedString(text).encode('utf-8')

def add_sort_methods():
    sort_methods = [xbmcplugin.SORT_METHOD_LABEL,xbmcplugin.SORT_METHOD_UNSORTED,xbmcplugin.SORT_METHOD_DATE,xbmcplugin.SORT_METHOD_DURATION,xbmcplugin.SORT_METHOD_EPISODE]
    for method in sort_methods:
        xbmcplugin.addSortMethod(int(sys.argv[1]), sortMethod=method)
    return
