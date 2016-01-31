#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


# returns a list of the absolute paths of the special files in the given directory
#
def get_special_paths(dir):
  filenames = os.listdir(dir)
  # print filenames

  # print os.path.abspath(dir)

  special_filenames = {}

  for filename in filenames:
    if filename.endswith(".jpg") or filename.endswith("txt"):
      special_filenames[os.path.abspath(os.path.join(dir, filename))] = filename
  return special_filenames


# given a list of paths, copies those files into the given directory
def copy_to(paths, todir):
  if os.path.exists(todir) != True:
    os.mkdir(todir)
  for special_file_path, special_filename in paths.iteritems():
    shutil.copy(special_file_path, todir + '/' + special_filename)

# given a list of paths, zip those files up into the given zipfile
def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' '
  for special_file_path, special_filename in paths.iteritems():
    cmd += ' \'' + special_file_path + '\''
  print "Command to run:", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)
  print output  ## Otherwise do something with the command's output


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir != '':
    for arg in args:
      special_filepaths = get_special_paths(arg)
      copy_to(special_filepaths, todir)
  elif tozip != '':
    for arg in args:
      special_filepaths = get_special_paths(arg)
      zip_to(special_filepaths, tozip)
  else:
    for arg in args:
      print get_special_paths(arg)
  
if __name__ == "__main__":
  main()
