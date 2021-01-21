import os
import sqlite3
##import re
import shutil

#pattern = 'https?:\/\/(?:w{1,3}\.)?[^\s.]+(?:\.[a-z]+)*(?::\d+)?(?![^<]*(?:<\/\w+>|\/?>))'
#tmp = re.findall(pattern, urls)

# EXCLUIR ARQUIVO
history = os.path.join("C:\\temp\\", "History.txt")
if os.path.exists(history):
    os.unlink(history)

history = os.environ['USERPROFILE'] + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
destination = "c:\\temp\\History"
shutil.copyfile(history,os.path.join(destination))

con = sqlite3.connect("C:\\Temp\\History")
cursor = con.cursor()
cursor.execute("SELECT url,title FROM urls")
urls = cursor.fetchall()

#f = open(history, "a")
for l in urls:
    print(str(l[0]) + "|" + str(l[1]))
#f.close

#print(urls)

