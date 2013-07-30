#! /usr/bin/env python

import zbar, os

proc = zbar.Processor ()

proc.parse_config ("enable")

device = "/dev/video0"

proc.init (device)

cmds = {"chrome": "google-chrome"}

def handle (proc, image, closure):
    for symbol in image.symbols:
        print symbol.data

        try:
            print "launching " + cmds[symbol.data]
            os.system (cmds[symbol.data] + " &")

        except Error as e:
            print "code " + symbol.data + " not found"

proc.set_data_handler (handle)
proc.visible = False
proc.active = True

try:
    proc.user_wait ()
except zbar.WindowClosed:
    pass
