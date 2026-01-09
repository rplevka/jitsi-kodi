#!/bin/bash

# Script to create a Kodi addon package for Jitsi Meet

ADDON_ID="plugin.video.jitsi"
VERSION="1.0.0"
PACKAGE_NAME="${ADDON_ID}-${VERSION}.zip"

echo "Creating Kodi addon package: ${PACKAGE_NAME}"
echo "============================================"

# Check if we're in the right directory
if [ ! -f "addon.xml" ]; then
    echo "Error: addon.xml not found. Please run this script from the addon root directory."
    exit 1
fi

# Create a temporary directory for packaging
TEMP_DIR=$(mktemp -d)
ADDON_DIR="${TEMP_DIR}/${ADDON_ID}"

echo "Copying files to temporary directory..."
mkdir -p "${ADDON_DIR}"

# Copy all necessary files
cp -r addon.xml addon.py resources LICENSE README.md "${ADDON_DIR}/"

# Remove any unwanted files
find "${ADDON_DIR}" -name "*.pyc" -delete
find "${ADDON_DIR}" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find "${ADDON_DIR}" -name ".DS_Store" -delete

# Create the zip file
echo "Creating ZIP package..."
cd "${TEMP_DIR}"
zip -r "${PACKAGE_NAME}" "${ADDON_ID}" -x "*.git*" -x "*.DS_Store" -x "*__pycache__*"

# Move the package to the original directory
mv "${PACKAGE_NAME}" "${OLDPWD}/"

# Clean up
cd "${OLDPWD}"
rm -rf "${TEMP_DIR}"

echo ""
echo "Package created successfully: ${PACKAGE_NAME}"
echo ""
echo "Installation instructions:"
echo "1. Copy ${PACKAGE_NAME} to your Kodi device"
echo "2. In Kodi, go to Settings > Add-ons > Install from zip file"
echo "3. Select ${PACKAGE_NAME}"
echo "4. Wait for the addon enabled notification"
echo ""
echo "Done!"
