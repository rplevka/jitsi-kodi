#!/bin/bash

# Script to create a Kodi addon package for Jitsi Meet

set -e  # Exit on error

ADDON_ID="plugin.video.jitsi"
VERSION="1.0.1"
PACKAGE_NAME="${ADDON_ID}-${VERSION}.zip"

echo "Creating Kodi addon package: ${PACKAGE_NAME}"
echo "============================================"

# Check if we're in the right directory
if [ ! -f "addon.xml" ]; then
    echo "Error: addon.xml not found. Please run this script from the addon root directory."
    exit 1
fi

# Check if zip command is available
if ! command -v zip &> /dev/null; then
    echo "Error: 'zip' command not found."
    echo ""
    echo "Please install zip using one of these methods:"
    echo "  - macOS: brew install zip"
    echo "  - Ubuntu/Debian: sudo apt-get install zip"
    echo "  - Fedora/RHEL: sudo dnf install zip"
    echo ""
    echo "Alternatively, manually create the package:"
    echo "  1. Create a directory named '${ADDON_ID}'"
    echo "  2. Copy addon.xml, addon.py, resources/, LICENSE, and README.md into it"
    echo "  3. Compress it to ${PACKAGE_NAME}"
    exit 1
fi

# Create a temporary directory for packaging
TEMP_DIR=$(mktemp -d)
ADDON_DIR="${TEMP_DIR}/${ADDON_ID}"

# Trap to ensure cleanup happens even on error
trap "cd '${OLDPWD}'; rm -rf '${TEMP_DIR}'" EXIT

echo "Copying files to temporary directory..."
mkdir -p "${ADDON_DIR}"

# Copy all necessary files
if ! cp -r addon.xml addon.py resources LICENSE README.md "${ADDON_DIR}/"; then
    echo "Error: Failed to copy files."
    exit 1
fi

# Remove any unwanted files
find "${ADDON_DIR}" -name "*.pyc" -delete
find "${ADDON_DIR}" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find "${ADDON_DIR}" -name ".DS_Store" -delete

# Create the zip file
echo "Creating ZIP package..."
cd "${TEMP_DIR}"

if ! zip -r "${PACKAGE_NAME}" "${ADDON_ID}" -x "*.git*" -x "*.DS_Store" -x "*__pycache__*"; then
    echo "Error: Failed to create ZIP package."
    exit 1
fi

# Move the package to the original directory
if ! mv "${PACKAGE_NAME}" "${OLDPWD}/"; then
    echo "Error: Failed to move package to destination."
    exit 1
fi

# Return to original directory (cleanup will happen via trap)
cd "${OLDPWD}"

echo ""
echo "✓ Package created successfully: ${PACKAGE_NAME}"
echo ""
echo "Installation instructions:"
echo "1. Copy ${PACKAGE_NAME} to your Kodi device"
echo "2. In Kodi, go to Settings > Add-ons > Install from zip file"
echo "3. Select ${PACKAGE_NAME}"
echo "4. Wait for the addon enabled notification"
echo ""
echo "Done!"
