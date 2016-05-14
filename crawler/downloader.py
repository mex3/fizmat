import subprocess
f=open("linkslist.txt", "r")
for x in f:
    subprocess.call(["C:\curl\curl.exe", x, '-o','--create-dirs', "file_#1.txt"],shell= True)#start cURL executable
f.close()
