#!/usr/bin/env python

#
# Usage:
#
#   ./setupVirtualenv.py [<no-arg>]
#

import os, sys

def message(s):
  print(">> " + s + "\n")

commands = [
  "source ~/.virtualenvs/bin/activate"
  # "pip install -r requirements.txt"
]

command = " && ".join(commands)

message("Usage: ./setupVirtualenv.py <no-arg> ")
message("Running:\n" + command)
os.system(command)
