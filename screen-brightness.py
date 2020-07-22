import os
import sys

brightness_level = float(sys.argv[1]) / 100

# run xrandr to find out your monitor names
sencond_monitor_name = 'HDMI-1'

os.popen('xrandr --output ' + sencond_monitor_name + ' --brightness ' + str(brightness_level))

