#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
   # Open file
  f = open(filename, 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  years = re.findall(r'(Popularity in)\s([\d]{4})(</h)', f.read())

  yearNo = years[0][1]

  print yearNo

  f = open(filename, 'r')

  babies = re.findall(r'(<tr align="right"><td>)(\d{1,6})(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', f.read())

  names_rank = {}
  for baby in babies:
    rank = baby[1]
    male_name = baby[3]
    female_name = baby[5]
    names_rank[male_name] = rank
    names_rank[female_name] = rank


  content = []
  content.append(yearNo)

  for name in sorted(names_rank):
    content.append(name + " " + names_rank[name])

  return content


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  if summary == True:
    print "bring it"
    for arg in args:
      print arg
      names = '\n'.join(extract_names(arg)) + '\n'
      f = open(arg + '.summary', 'w')
      f.write(names)
      f.close()
  else:
    for arg in args:
      print arg
      print '\n'.join(extract_names(arg)) + '\n'

  
if __name__ == '__main__':
  main()
