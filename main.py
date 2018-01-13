from solution import parser, Part1, part_2A, part_2B
import re
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
parser.parse2ds('ptb.train.txt')
with open('dataset_spaceless.txt', 'r') as fh:
    dataset = fh.read()
counts = part_2A.get_count(dataset)

part2data = parser.parse2('input')
with open(outputdir + '/2a.out', 'a') as out2a:
    for e in part2data:
        val = part_2A.parse_input(e[1])
        if e[0] == 'PTB':
            out2a.write((str(counts[val]) if val in counts else str(0)) + '\n')
        else:
            thesecounts = part_2A.get_count(re.sub('[^a-zA-Z]', '', e[0]))
            out2a.write((str(thesecounts[val]) if val in thesecounts else str(0)) + '\n')

part2bdata = parser.parse2b('input')
with open(outputdir + '/2b.out', 'a') as out2b:
    for e in part2bdata:
        val = part_2B.part_2B(counts, e[0], e[1])
        out2b.write(str(val) + '\n')
        
with open('input/3a.in', 'r') as fh:
    import re
    res = []
    data = fh.read().upper().split('\n')
    for e in data:
        if e == '': continue
        j= re.sub('[^a-zA-Z \|]', '', e)         # Remove non-alpha characters
        res.append(j)
        
with open(outputdir + '/3a.out', 'a') as out3a:
    for e in res:
        val = SimpleCrack.SimpleCrack(counts, e)
        out3a.append(str(val[0]) + '|' + val[1])