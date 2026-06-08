#!/usr/bin/env python

import sys
import os

root_dir = os.path.abspath(os.path.dirname(__file__))
lib_dir = os.path.join(root_dir, 'lib')
sys.path.insert(0, lib_dir)

from libpypack.application import Application

pypack = Application(root_dir)
pypack.run()
