#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# Returns a list of the puzzle urls from the given log file,
# extracting the hostname from the filename itself.
# Screens out duplicate urls and returns the urls sorted into
# increasing order."""
def read_urls(filename):

  print "filename: " +  filename.split("_")[1]

  http_path = "http://" + filename.split("_")[1]

  print "filename: " +  http_path

  f = open(filename, 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  # years = re.findall(r'(Popularity in)\s([\d]{4})(</h)', f.read())

  lines_with_puzzle = 0
  strings = []

  for line in f:   ## iterates over the lines of the file
    if line.find('puzzle') == -1: continue;
    lines_with_puzzle += 1;
    # match = re.search(r'(GET)(.*\.jpg)(HTTP)', line)
    match = re.search(r'(GET\s)([a-z/-]*\.jpg)(\sHTTP)', line)
    if match == None : continue
    # print match.group(2)
    image_slice_url = http_path + match.group(2)
    if image_slice_url in strings: continue;
    strings.append(image_slice_url)

  print lines_with_puzzle
  print len(strings)

  return sorted(strings)

  # +++your code here+++
  
# Given the urls already in the correct order, downloads
# each image into the given directory.
# Gives the images local filenames img0, img1, and so on.
# Creates an index.html in the directory
# with an img tag to show each local image file.
# Creates the directory if necessary.
def download_images(img_urls, dest_dir):
  if os.path.exists(dest_dir) != True:
    os.mkdir(dest_dir)

  f = open(dest_dir + '/index.html', 'w')

  index_html_content = "<verbatim><html><body>"

  i = 0;
  for img_url in img_urls:
    img_name = "img" + str(i) + ".jpg"
    print '\n' + "Retrieving" + img_url + " saving as " + img_name + " ..."
    urllib.urlretrieve(img_url, dest_dir + "/" + img_name)
    index_html_content += "<img src=\"" + img_name + "\">"
    i+=1

  index_html_content += "</body></html>"

  f.write(index_html_content)
  f.close()
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
