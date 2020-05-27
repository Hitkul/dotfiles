#!/usr/bin/env python3
#
# Copyright (C) 2016 James Murphy
# Licensed under the GPL version 2 only
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output

items = check_output("upower --dump", shell=True).rstrip()

cut_string = "Device: /org/freedesktop/UPower/devices/mouse_hidpp_battery_0"
items =  str(items)
items = items[items.index(cut_string):]
cut_string = "percentage"
items = items[items.index(cut_string):]
items = items[:items.index("\\n")]
percentleft = int(items.split(" ")[-1].replace("%",''))

def color(percent):
    if percent < 10:
        # exit code 33 will turn background red
        return "#FFFFFF"
    if percent < 20:
        return "#FF3300"
    if percent < 30:
        return "#FF6600"
    if percent < 40:
        return "#FF9900"
    if percent < 50:
        return "#FFCC00"
    if percent < 60:
        return "#FFFF00"
    if percent < 70:
        return "#FFFF33"
    if percent < 80:
        return "#FFFF66"
    return "#FFFFFF"

form =  '<span color="{}">{}%</span>'
fulltext = form.format(color(percentleft), percentleft)
print(fulltext)
# print(fulltext)