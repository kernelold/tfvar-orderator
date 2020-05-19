#!/usr/bin/env python3
import hcl
from collections import OrderedDict
import sys

filename = sys.argv[1]

with open(filename, 'r') as fp:
    obj = hcl.load(fp)
    variables = OrderedDict(obj['variable'])
    for i in variables:
      content = variables[i]
      vartype = variables[i]['type']
      z = ""
      if vartype == "string":
        quoted  = True
      else:
        quoted = False
      for c in content:
        value = content[c]
        if c == "type":
          z = z + '\n  ' + str(c) + ' = ' + str(value)
        elif c == "description":
          z = z + '\n  ' + str(c) + ' = "' + str(value) + '"'
        else:
          if value == 'null':
            z = z + '\n  ' + str(c) + ' = ' + str(value)
          else:
            if quoted == True:
              z = z + '\n  ' + str(c) + ' = "' + str(value) + '"'
            else:
              z = z + '\n  ' + str(c) + ' = ' + str(value)
      print('variable "' + i + '" {' + z + '\n' + '}' )
