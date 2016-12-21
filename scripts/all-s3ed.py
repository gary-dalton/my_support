#!/bin/python
"""
all-s3ed.py: Generates the set difference to create the todo_sites file.
"""

file1 = "s3ed_sites.txt"
file2 = "all_sites.txt"
file3 = "todo_sites.txt"

with open(file1) as f:
  done =  f.read().splitlines()

with open(file2) as f:
  all =  f.read().splitlines()

todo = set(all).difference(done)
with open(file3, 'w') as f:
  f.write('\n'.join(todo))