# -*- coding: utf-8 -*-
"""
Author: Graham Hoyes

Description: File parser
"""

import os
import re

res = {'1a': {'ENCRYPT': [], 'DECRYPT': []}, '1b': {'ENCRYPT': [], 'DECRYPT': []}, '1c':{'ENCRYPT': [], 'DECRYPT': []}}

inputdir = 'input'
files1 = ['1a.in', '1b.in', '1c.in']
files2 = ['2a.in', '2b.in']
files3 = ['3a.in', '3b.in', '3c.in', '3d.in']

## Parsing for part 1
for file in files1:
    with open(inputdir + '/' + file) as fh:
        data = fh.read().upper().split('\n')
    for e in data:
        if e == '': break                           # empty line
        instr = e.split(' | ')
        if instr[1].find(' ') >= 0:                  # Dealing with 1b
            if instr[0] == 'ENCRYPT':
                res['1b']['ENCRYPT'].append([[int(e) for e in instr[1].split(' ')], instr[2]])
            elif instr[0] == 'DECRYPT':
                res['1b']['DECRYPT'].append([[int(e) for e in instr[1].split(' ')], instr[2]])
        elif len(instr[1]) == 26:               # Dealing with 1c
            if instr[0] == 'ENCRYPT':           # Should I process non-alpha out of here?
                res['1c']['ENCRYPT'].append([instr[1], instr[2]])
            elif instr[0] == 'DECRYPT':
                res['1c']['DECRYPT'].append([instr[1], instr[2]])
        else:                                   # Dealing with 1a
            if instr[0] == 'ENCRYPT':
                res['1a']['ENCRYPT'].append([int(instr[1]), instr[2]])
            elif instr[0] == 'DECRYPT':
                res['1a']['DECRYPT'].append([int(instr[1]), instr[2]])

## Parse the big ass data file for part 2
with open('ptb.train.txt') as fh:
    rawtrain = fh.read();
    train = re.sub('N |<unk> ', '', rawtrain)       # Remove all cases of N or <unk> followed by a space
    train = re.sub(' N| <unk>', '', train)       # Remove all cases of N or <unk> preceeded by a space
    train = re.sub('[^a-zA-Z ]', '', train)          # Remove all non-alpha characters, preserve spaces
    train = train.upper()
with open('dataset.txt', 'w') as fh:
    fh.write(train)  
