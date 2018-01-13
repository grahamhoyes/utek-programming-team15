# -*- coding: utf-8 -*-
"""
Author: Graham Hoyes

Description: File parser
"""

def parse1(inputdir):    
    res = {'1a': [], '1b': [], '1c':[]}
    
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
            if file == '1b.in':                  # Dealing with 1b
                res['1b'].append([instr[0], [int(e) for e in instr[1].split(' ')], instr[2]])
            elif file == '1c.in':               # Dealing with 1c
                res['1c'].append([instr[0], instr[1], instr[2]])
            else:                                   # Dealing with 1a
                res['1a'].append([instr[0], int(instr[1]), instr[2]])  
    
    return res;

def parse2(ds):
    ## Parse the big data file for part 2
    import re
    with open(ds) as fh:
        rawtrain = fh.read();
        train = re.sub('N |<unk> ', '', rawtrain)       # Remove all cases of N or <unk> followed by a space
        train = re.sub(' N| <unk>', '', train)          # Remove all cases of N or <unk> preceeded by a space
        train = re.sub('[^a-zA-Z ]', '', train)         # Remove all non-alpha characters, preserve spaces
        train = re.sub('  +', ' ', train)
        train = train.upper()
    with open('dataset.txt', 'w') as fh:
        fh.write(train)