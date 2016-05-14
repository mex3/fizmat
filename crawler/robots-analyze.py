
def remove_string(filename, string):
    rst = []
    with open(filename) as fd:
        t = fd.read()
        for line in t.splitlines():
            if line != string:
                rst.append(line)

    with open(filename, 'w') as fd:
        fd.write('\n'.join(rst))
        fd.write('\n')
import subprocess
subprocess.call(["C:\curl\curl.exe",'http://informatics.mccme.ru/robots.txt', '-o', 'robots.txt' ], shell=True)
f = open('linksraw.txt', 'r')
d = open('linkslist.txt', 'a')
x = open('robots.txt')
for paths in x:
    if 'Disallow:' in paths:
        paths = paths.strip()
        paths = ''.join(paths.split(':')[1:])
        for links in f:
            if paths in links:
                remove_string('linksraw.txt',links)
f.close()
f = open('linksraw.txt', 'r')
for links in f:
    d.write(links)
d.close()
f.close()