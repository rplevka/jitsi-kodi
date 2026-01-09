# Media Assets

This directory should contain the following image files for the addon:

## Required Files

### icon.png
- **Size**: 256x256 pixels (or 512x512 for high-DPI displays)
- **Format**: PNG with transparency
- **Description**: The addon icon displayed in Kodi's addon browser
- **Suggested content**: Jitsi Meet logo or a video conference icon

### fanart.jpg
- **Size**: 1920x1080 pixels (16:9 aspect ratio)
- **Format**: JPEG or PNG
- **Description**: Background artwork displayed when the addon is selected
- **Suggested content**: Abstract background or Jitsi Meet branding

## Creating Assets

You can create these assets using:
- Image editing software (GIMP, Photoshop, etc.)
- Online tools like Canva or Figma
- Jitsi Meet official branding assets (with proper attribution)

## Placeholder Assets

Until custom assets are created, Kodi will use default icons. The addon will function normally without these files, but custom assets improve the user experience.

## License Considerations

If using Jitsi Meet branding:
- Jitsi Meet is open source (Apache 2.0 license)
- Follow their branding guidelines
- Provide proper attribution

## File Paths

These files are referenced in `addon.xml`:
```xml
<assets>
    <icon>resources/media/icon.png</icon>
    <fanart>resources/media/fanart.jpg</fanart>
</assets>
```
