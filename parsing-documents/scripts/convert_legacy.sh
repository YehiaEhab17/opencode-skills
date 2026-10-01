#!/bin/bash

# convert_legacy.sh
# Uses LibreOffice to convert .doc/.ppt to .docx/.pptx
# Automatically downloads a portable AppImage to the scripts folder if needed.

if [ -z "$1" ]; then
  echo "Error: No file path provided."
  echo "Usage: ./convert_legacy.sh /path/to/file.doc"
  exit 1
fi

FILE_PATH="$1"
DIR_NAME=$(dirname "$FILE_PATH")
EXT="${FILE_PATH##*.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
APPIMAGE_PATH="$SCRIPT_DIR/LibreOffice.AppImage"

if [[ "$EXT" != "doc" && "$EXT" != "ppt" ]]; then
  echo "Warning: File extension is not .doc or .ppt. Proceeding anyway, but it may not be necessary."
fi

# 1. Determine which LibreOffice to use
if command -v libreoffice &> /dev/null; then
    LO_CMD="libreoffice"
elif command -v soffice &> /dev/null; then
    LO_CMD="soffice"
elif [ -f "$APPIMAGE_PATH" ]; then
    LO_CMD="$APPIMAGE_PATH"
else
    echo "LibreOffice not found globally. Downloading portable AppImage to $SCRIPT_DIR..."
    # Download a reliable LibreOffice AppImage (Fresh branch)
    wget -q --show-progress -O "$APPIMAGE_PATH" "https://libreoffice.soluzioniopen.com/stable/basic/LibreOffice-fresh.basic-x86_64.AppImage"
    
    if [ ! -f "$APPIMAGE_PATH" ]; then
        echo "Error: Failed to download LibreOffice AppImage."
        exit 1
    fi
    chmod +x "$APPIMAGE_PATH"
    LO_CMD="$APPIMAGE_PATH"
    echo "Download complete."
fi

echo "Converting $FILE_PATH using $LO_CMD..."

# Run the conversion
"$LO_CMD" --headless --convert-to "${EXT}x" "$FILE_PATH" --outdir "$DIR_NAME"

if [ $? -eq 0 ]; then
  echo "Conversion successful. Saved to $DIR_NAME"
else
  echo "Error: Conversion failed."
  exit 1
fi