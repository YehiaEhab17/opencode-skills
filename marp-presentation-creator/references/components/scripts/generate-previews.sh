#!/bin/bash
# Generate PDF previews for all components
# Run this from the components/ directory
# Usage: bash scripts/generate-previews.sh

COMPONENTS_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$COMPONENTS_DIR"

echo "Generating PDF previews for all components..."
echo ""

for dir in */; do
  # Skip scripts/ and non-directories
  [ "$dir" = "scripts/" ] && continue
  [ ! -f "${dir}preview.md" ] && continue
  
  component_name="$(basename "$dir")"
  echo "  Compiling: $component_name ..."
  npx @marp-team/marp-cli "${dir}preview.md" -o "${dir}preview.pdf" --allow-local-files 2>/dev/null
  if [ $? -eq 0 ]; then
    echo "  ✓ $component_name done"
  else
    echo "  ✗ $component_name FAILED"
  fi
  echo ""
done

echo "All previews generated!"
