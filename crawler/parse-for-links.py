import re
p = re.compile('<a\s*href\s*=\s*["](.*)["]\s*>')
f = open('file_#1.txt', 'r', encoding= 'utf-8')
d = open('linksraw.txt', 'w')
for line in f:
    x = ''.join(p.findall(line))
    if x != '':
        d.write(x+'\n')
d.close()
f.close()

