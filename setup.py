__author__ = 'hzsunyuda'

from distutils.core import setup
import py2exe
includes = ["encodings", "encodings.*"]
options = {"py2exe":
               {
                   "includes":includes,
                   "bundle_files":1
               }}

# setup(console=["update.py"])
setup(console=["ui.py"])