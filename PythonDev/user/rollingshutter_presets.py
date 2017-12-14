# rollingshutter_presets.py
# Author: 
# Michael McReynolds
# itaki design studio
# itaki.com
#
# v1
# 09/08/2014
#
# user presets for RollingShurtter plugin
#
# only works with Nuke 6.3v1 and above
# Install Instructions:
# 1. copy the file into your .nuke folder or anywhere in your NUKE_PATH 
# 2. in your init.py or menu.py put the following code:
# import rollingshutter_presets
# rollingshutter_presets.nodePresetRollingShutter()
#
# Any issues or additional cameras you would like added to this tool then email me or post a reply in the comments on nukepedia
# I got these values from http://www.reduser.net/forum/showthread.php?74399-Scarlets-Rolling-Shutter-Value-for-Foundry-Plug-In&s=c0394f4c2e420553bb0c3cab41e3e043
# 
#

import nuke
def nodePresetRollingShutter():
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Canon/5D MKII", {'correction': '.56', 'label': 'Canon 5D MKII', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Canon/7D", {'correction': '.62', 'label': 'Canon 7D', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "RED/ONE", {'correction': '.32', 'label': 'RED ONE', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "RED/ONE MX (F/W 30.6.10#30)", {'correction': '.56', 'label': 'ONE MX (F/W 30.6.10#30)', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Panasonic/Lumix GH2 without ETC ", {'correction': '.59', 'label': 'Panasonic Lumix GH2 without ETC', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Panasonic/Lumix GH2 with ETC 1:1 mode in 1080p", {'correction': '.34', 'label': 'Panasonic Lumix GH2 with ETC 1:1 mode in 1080p', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Panasonic/Lumix GH2 with ETC 1:1 mode in 720p", {'correction': '.60', 'label': 'Panasonic Lumix GH2 with ETC 1:1 mode in 720p', 'note_font': 'Helvetica'})
  nuke.setPreset("OFXuk.co.thefoundry.rollingshutter.rollingshutter_v100", "Sony/PMW EX-1", {'correction': '.38', 'label': 'Sony PMW EX-1', 'note_font': 'Helvetica'})
 