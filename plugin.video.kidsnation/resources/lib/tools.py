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
import base64
from glo_var import *
#######################################################################

#######################################################################
# YouTube API Settings
DATA_API      = base64.b64decode(b'QUl6YVN5QXMtdkRyWDNXdnZCQzdMcUMxUWFhOFZHUVFmRWdMRlJB')
DATA_CLIENT   = base64.b64decode(b'MTgzMTY1MzQzMjQ0LXY5MDFhNWFmbXNla212NjlycGJkOHNlM2ZwYW1wcG1oLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29t')
DATA_SECRET   = base64.b64decode(b'M3k1YWkzZFhMUkhVbG5rV3YtLTlpNDho')
#######################################################################

def Apply_API():
    __settings__ = xbmcaddon.Addon(id='plugin.video.youtube')
    __settings__.setSetting("youtube.api.enable", 'true')
    __settings__.setSetting("youtube.api.last.switch", 'own')
    __settings__.setSetting("youtube.api.key", DATA_API)
    __settings__.setSetting("youtube.api.id", DATA_CLIENT)
    __settings__.setSetting("youtube.api.secret", DATA_SECRET)
    ytDialog = xbmcgui.Dialog()
    ytDialog.ok(ADDONTITLE, '[COLOR springgreen]YouTube API Keys Set To ' + ADDONTITLE + '[/COLOR]')