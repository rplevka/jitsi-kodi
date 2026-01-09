import xbmc
import xbmcgui
import xbmcaddon
import json
import os

ADDON = xbmcaddon.Addon()
ADDON_DATA_PATH = xbmc.translatePath(ADDON.getAddonInfo('profile'))
RECENT_ROOMS_FILE = os.path.join(ADDON_DATA_PATH, 'recent_rooms.json')

class JitsiClient:
    def __init__(self):
        self.server = ADDON.getSetting('jitsi_server') or 'https://meet.jit.si'
        self.display_name = ADDON.getSetting('display_name') or 'Kodi User'
        
        if not os.path.exists(ADDON_DATA_PATH):
            os.makedirs(ADDON_DATA_PATH)
    
    def join_room(self, room_name):
        url = f"{self.server}/{room_name}"
        self._save_recent_room(room_name)
        self._open_jitsi_url(url)
    
    def join_by_url(self, url):
        room_name = url.split('/')[-1]
        self._save_recent_room(room_name)
        self._open_jitsi_url(url)
    
    def _open_jitsi_url(self, url):
        config_params = []
        
        if self.display_name:
            config_params.append(f"config.prejoinPageEnabled=false")
            config_params.append(f"userInfo.displayName={self.display_name}")
        
        if ADDON.getSetting('start_audio_muted') == 'true':
            config_params.append("config.startWithAudioMuted=true")
        
        if ADDON.getSetting('start_video_muted') == 'true':
            config_params.append("config.startWithVideoMuted=true")
        
        if config_params:
            separator = '&' if '?' in url else '#'
            url = f"{url}{separator}{'&'.join(config_params)}"
        
        xbmc.log(f"[Jitsi Meet] Opening URL: {url}", xbmc.LOGINFO)
        
        dialog = xbmcgui.Dialog()
        dialog.notification(
            'Jitsi Meet',
            f'Opening meeting in browser...',
            xbmcgui.NOTIFICATION_INFO,
            3000
        )
        
        xbmc.executebuiltin(f'RunPlugin(plugin://plugin.program.chrome.launcher/?{url})')
        
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            xbmc.log(f"[Jitsi Meet] Error opening browser: {str(e)}", xbmc.LOGERROR)
            dialog.ok('Error', f'Could not open browser. Please visit:\n{url}')
    
    def get_recent_rooms(self):
        if os.path.exists(RECENT_ROOMS_FILE):
            try:
                with open(RECENT_ROOMS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_recent_room(self, room_name):
        recent_rooms = self.get_recent_rooms()
        
        if room_name in recent_rooms:
            recent_rooms.remove(room_name)
        
        recent_rooms.insert(0, room_name)
        recent_rooms = recent_rooms[:10]
        
        with open(RECENT_ROOMS_FILE, 'w') as f:
            json.dump(recent_rooms, f)
