#!/bin/bash
# Launch minimal Chromium in kiosk mode on framebuffer
xinit /usr/bin/chromium \
  --kiosk \
  --no-sandbox \
  --disable-infobars \
  --autoplay-policy=no-user-gesture-required \
  file:///opt/alienpc/boot-splash.html \
  -- :0 vt7 &

# Play audio simultaneously
aplay /opt/alienpc/boot-sounds/alienpc-boot.ogg &

# Kill after 5 seconds
sleep 5
pkill -f boot-splash.html
