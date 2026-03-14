#!/usr/bin/env python3
"""
Composite a generated photo with a UI template overlay.

Usage:
  python3 scripts/composite.py <photo> <template> <output>

Examples:
  # Single video
  python3 scripts/composite.py videos/002-rubber-duck/camera.jpeg templates/camera-screen.png videos/002-rubber-duck/camera-final.png

  # All videos (from shorts-factory directory)
  for dir in videos/*/; do
    name=$(basename "$dir")
    if [ -f "$dir/camera.jpeg" ]; then
      python3 scripts/composite.py "$dir/camera.jpeg" templates/camera-screen.png "$dir/camera-final.png"
      echo "Done: $name"
    fi
  done
"""

import sys
from PIL import Image


def composite(photo_path, template_path, output_path):
    template = Image.open(template_path).convert("RGBA")
    photo = Image.open(photo_path).convert("RGBA")

    tw, th = template.size
    pw, ph = photo.size

    # Crop-to-fill: scale photo to cover template, then center-crop
    scale = max(tw / pw, th / ph)
    new_w = int(pw * scale)
    new_h = int(ph * scale)
    photo_resized = photo.resize((new_w, new_h), Image.LANCZOS)

    left = (new_w - tw) // 2
    top = (new_h - th) // 2
    photo_cropped = photo_resized.crop((left, top, left + tw, top + th))

    # Layer template on top of photo
    result = Image.alpha_composite(photo_cropped, template)
    result.save(output_path)
    print(f"{output_path} ({tw}x{th})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 scripts/composite.py <photo> <template> <output>")
        sys.exit(1)

    composite(sys.argv[1], sys.argv[2], sys.argv[3])
