#! /usr/bin/env python

import zbar, os, sys

proc = zbar.Processor ()

proc.parse_config ("enable")

device = "/dev/video0"

proc.init (device)

cards = {
    "02S": "remote;willisson.org",
    "03S": "remote;pacew.dyndns.org",
    "04S": "athena.dialup.mit.edu",
    "05S": "",
    "06S": "",
    "07S": "",
    "08S": "",
    "09S": "",
    "10S": "",
    "JS": "",
    "QS": "exec;emacs",
    "KS": "exec;xterm",
    "AS": "exec;google-chrome",

    "02C": "val;2",
    "03C": "val;3",
    "04C": "val;4",
    "05C": "val;5",
    "06C": "val;6",
    "07C": "val;7",
    "08C": "val;8",
    "09C": "val;9",
    "10C": "val;10",
    "JC": "val;11",
    "QC": "val;12",
    "KC": "val;13",
    "AC": "val;14",

    "02D": "",
    "03D": "",
    "04D": "",
    "05D": "",
    "06D": "",
    "07D": "",
    "08D": "",
    "09D": "",
    "10D": "",
    "JD": "",
    "QD": "",
    "KD": "",
    "AD": "",

    "02H": "",
    "03H": "",
    "04H": "",
    "05H": "",
    "06H": "",
    "07H": "",
    "08H": "",
    "09H": "",
    "10H": "",
    "JH": "",
    "QH": "",
    "KH": "",
    "AH": "",

    "REDJOKER": "",
    "BLACKJOKER": ""
}


def handle (proc, image, closure):
    global val

    for symbol in image.symbols:
        try:
            card = cards[symbol.data]

            tokens = card.split (";")

            if tokens[0] == "exec":
                for i in range (val):
                    print "launching " + tokens[1]
                    os.system (tokens[1] + " >/dev/null 2>&1 &")

                val = 1
            elif tokens[0] == "val":
                print "set val to " + tokens[1]
                val = int (tokens[1])
            elif tokens[0] == "remote":
                server = tokens[1]
                print "syncing tmp dirs"
                os.system ("rsync -avz /home/atw/tmp " + server + ":. >/dev/null 2>&1")

        except:
            pass

val = 1

proc.set_data_handler (handle)
proc.visible = False
proc.active = True

try:
    proc.user_wait ()
except:
    sys.exit (0)
