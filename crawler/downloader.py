import subprocess
f=open("linkslist.txt", "r")
for x in f:
    subprocess.call(["C:\Users\mihalev_n\Documents\cURL\curl.exe", x, '-o', "file_#1.txt"],shell= True)#start cURL executable
f.close()
#http://www.py-my.ru/post/4bfb3c6a1d41c846bc00009b
