import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
from urllib.parse import parse_qsl, urlencode
from resources.lib.jitsi_client import JitsiClient

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path')

def get_url(**kwargs):
    return '{}?{}'.format(sys.argv[0], urlencode(kwargs))

def list_main_menu():
    xbmcplugin.setPluginCategory(int(sys.argv[1]), ADDON_NAME)
    xbmcplugin.setContent(int(sys.argv[1]), 'videos')
    
    items = [
        {
            'label': 'Join Room',
            'url': get_url(action='join_room'),
            'is_folder': False,
            'icon': 'DefaultVideo.png'
        },
        {
            'label': 'Join by URL',
            'url': get_url(action='join_url'),
            'is_folder': False,
            'icon': 'DefaultNetwork.png'
        },
        {
            'label': 'Recent Rooms',
            'url': get_url(action='recent_rooms'),
            'is_folder': True,
            'icon': 'DefaultRecentlyAddedEpisodes.png'
        },
        {
            'label': 'Settings',
            'url': get_url(action='settings'),
            'is_folder': False,
            'icon': 'DefaultAddonService.png'
        }
    ]
    
    for item in items:
        list_item = xbmcgui.ListItem(label=item['label'])
        list_item.setArt({'icon': item['icon']})
        list_item.setInfo('video', {'title': item['label']})
        xbmcplugin.addDirectoryItem(
            int(sys.argv[1]),
            item['url'],
            list_item,
            item['is_folder']
        )
    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def join_room():
    keyboard = xbmc.Keyboard('', 'Enter Room Name')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        room_name = keyboard.getText()
        if room_name:
            client = JitsiClient()
            client.join_room(room_name)

def join_url():
    keyboard = xbmc.Keyboard('https://meet.jit.si/', 'Enter Jitsi Meet URL')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        url = keyboard.getText()
        if url:
            client = JitsiClient()
            client.join_by_url(url)

def show_recent_rooms():
    xbmcplugin.setPluginCategory(int(sys.argv[1]), 'Recent Rooms')
    xbmcplugin.setContent(int(sys.argv[1]), 'videos')
    
    client = JitsiClient()
    recent_rooms = client.get_recent_rooms()
    
    for room in recent_rooms:
        list_item = xbmcgui.ListItem(label=room)
        list_item.setInfo('video', {'title': room})
        url = get_url(action='join_specific_room', room=room)
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, list_item, False)
    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def join_specific_room(room_name):
    client = JitsiClient()
    client.join_room(room_name)

def open_settings():
    ADDON.openSettings()

def router(paramstring):
    params = dict(parse_qsl(paramstring))
    
    if not params:
        list_main_menu()
    elif params['action'] == 'join_room':
        join_room()
    elif params['action'] == 'join_url':
        join_url()
    elif params['action'] == 'recent_rooms':
        show_recent_rooms()
    elif params['action'] == 'join_specific_room':
        join_specific_room(params['room'])
    elif params['action'] == 'settings':
        open_settings()

if __name__ == '__main__':
    router(sys.argv[2][1:])
