from solution import parser, Part1

outputdir = 'output'

part1data = parser.parse1('input')

## Part 1a
with open(outputdir + '/1a.out', 'a') as out1a:
    for e in part1data['1a']:
        if e[0] == 'ENCRYPT':
            out1a.write(Part1.SimpleEncrypt(e[1], e[2]) + '\n')
        elif e[0] == 'DECRYPT':
            out1a.write(Part1.SimpleDecrypt(e[1], e[2]) + '\n')

## Part 1b
with open(outputdir + '/1b.out', 'a') as out1b:
    for e in part1data['1b']:
        if e[0] == 'ENCRYPT':
            out1b.write(Part1.BlockEncrypt(e[1], e[2]) + '\n')
        elif e[0] == 'DECRYPT':
            out1b.write(Part1.BlockDecrypt(e[1], e[2]) + '\n')
            
## Part 1c
with open(outputdir + '/1c.out', 'a') as out1c:
    for e in part1data['1c']:
        if e[0] == 'ENCRYPT':
            out1c.write(Part1.PermutationEncrypt(e[1], e[2]) + '\n')
        elif e[0] == 'DECRYPT':
            out1c.write(Part1.PermutationDecrypt(e[1], e[2]) + '\n')
            
## Dataset for Part 2
parser.parse2('ptb.train.txt')
