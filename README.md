# Jitsi Meet for Kodi

A Kodi addon that allows you to join Jitsi Meet video conferences directly from your Kodi media center.

## Features

- Join Jitsi Meet rooms by name or URL
- Configurable Jitsi server (default: meet.jit.si)
- Custom display name
- Recent rooms history (stores last 10 rooms)
- Audio/video mute options
- Simple and intuitive interface

## Installation

### From ZIP file
1. Download the latest release ZIP file
2. In Kodi, go to Settings > Add-ons > Install from zip file
3. Select the downloaded ZIP file
4. Wait for the addon enabled notification

### Manual Installation
1. Clone this repository to your Kodi addons directory:
   - **Linux**: `~/.kodi/addons/plugin.video.jitsi/`
   - **Windows**: `%APPDATA%\Kodi\addons\plugin.video.jitsi\`
   - **macOS**: `~/Library/Application Support/Kodi/addons/plugin.video.jitsi/`
2. Restart Kodi or refresh addons

### Creating a ZIP for Installation
```bash
cd /path/to/jitsi-kodi
zip -r plugin.video.jitsi-1.0.0.zip . -x "*.git*" -x "*.DS_Store" -x "__pycache__/*"
```

## Usage

1. Launch the addon from Video Add-ons
2. Choose an option:
   - **Join Room**: Enter a room name to join
   - **Join by URL**: Paste a complete Jitsi Meet URL
   - **Recent Rooms**: Access previously joined rooms
   - **Settings**: Configure the addon

## Configuration

Access settings through the addon menu or Kodi's addon settings:

### General Settings
- **Jitsi Server URL**: Custom Jitsi server (default: https://meet.jit.si)
- **Display Name**: Your name in meetings (default: Kodi User)

### Meeting Options
- **Start with Audio Muted**: Join with microphone muted
- **Start with Video Muted**: Join with camera off

## Requirements

- Kodi 19 (Matrix) or later with Python 3.x support
- Python 3.x
- Internet connection
- Web browser (for opening Jitsi Meet interface)
- `script.module.requests` addon (usually pre-installed)

## How It Works

This addon integrates Jitsi Meet into Kodi by:
1. Providing a user-friendly interface for entering room names or URLs
2. Building properly formatted Jitsi Meet URLs with configuration parameters
3. Opening the meeting in your system's default web browser
4. Tracking recently joined rooms for quick access

The addon opens Jitsi Meet in your system's default web browser since Kodi doesn't natively support WebRTC, which is required for video conferencing.

## File Structure

```
plugin.video.jitsi/
├── addon.xml                    # Addon manifest
├── addon.py                     # Main entry point
├── resources/
│   ├── settings.xml            # Settings configuration
│   ├── language/
│   │   └── resource.language.en_gb/
│   │       └── strings.po      # English strings
│   ├── lib/
│   │   ├── __init__.py
│   │   └── jitsi_client.py    # Jitsi Meet integration
│   └── media/
│       ├── icon.png            # Addon icon (256x256)
│       └── fanart.jpg          # Background art (1920x1080)
├── LICENSE
└── README.md
```

## Notes

- This addon opens Jitsi Meet in your system's default web browser
- For best experience, ensure your system has a compatible browser installed (Chrome, Firefox, Safari, Edge)
- Audio/video functionality depends on your browser and hardware support
- Recent rooms are stored locally in Kodi's addon data directory

## Troubleshooting

### Browser doesn't open
- Ensure you have a default web browser set on your system
- Check Kodi logs for error messages
- The URL will be displayed in a dialog if the browser fails to open

### Import errors (xbmc, xbmcgui, etc.)
- These are expected when developing outside of Kodi
- The addon will work correctly when installed in Kodi
- These modules are provided by the Kodi runtime environment

### Settings not saving
- Ensure Kodi has write permissions to its addon data directory
- Check that the addon is properly installed

## Development

### Lint Warnings
The lint warnings about missing `xbmc*` modules are expected during development. These modules are provided by Kodi at runtime and are not available in standard Python environments.

### Testing
To test the addon:
1. Copy the addon directory to your Kodi addons folder
2. Restart Kodi or refresh addons
3. Enable the addon in Kodi's addon browser
4. Test functionality through the Kodi interface

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for Improvement
- Add support for custom Jitsi server configurations
- Implement in-Kodi video player integration (if WebRTC support becomes available)
- Add more language translations
- Create custom icon and fanart graphics
- Add support for password-protected rooms
- Implement room favorites/bookmarks

## Support

For issues and feature requests, please use the GitHub issue tracker at:
https://github.com/rplevka/jitsi-kodi/issues

## Credits

- Jitsi Meet: https://jitsi.org/
- Kodi: https://kodi.tv/

## Changelog

### v1.0.0 (2026-01-09)
- Initial release
- Basic room joining functionality
- Settings for server URL and display name
- Recent rooms tracking
- Audio/video mute options
