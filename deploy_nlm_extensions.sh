#!/bin/bash
set -euo pipefail

# Extension deployment launcher
# Architecture: x64/ARM64 compatible

URL_KORTEX="https://chromewebstore.google.com/detail/kortex-notebooklm/hdapplggdhndkblofffknpmnnnnbncbn"
URL_IMPORTER="https://chromewebstore.google.com/detail/notebooklm-web-importer/ijdefdijdmghafocfmmdojfghnpelnfn"
URL_EXPORTER="https://chromewebstore.google.com/detail/notebooklm-ultra-exporter/afchokljnhhggkhedfbmkcmdagjmjchj"

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start chrome "$URL_KORTEX" "$URL_IMPORTER" "$URL_EXPORTER"
elif [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "linux-android"* ]]; then
    xdg-open "$URL_KORTEX" & xdg-open "$URL_IMPORTER" & xdg-open "$URL_EXPORTER" &
else
    echo "Unsupported OS for automated browser launch. Manually navigate to URLs."
    exit 1
fi
