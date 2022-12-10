import os
import time
"""
print(os.getcwd())
os.chdir('C:\\Users\\vdi-student\\Desktop')
os.mkdir('nowy folder')
time.sleep(5)
os.rename('nowy folder','nowyfolder2')
time.sleep(5)
os.rmdir('nowyfolder2')
"""
os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop\\. && dir /s new.txt >> result.txt"')
# os.system('cmd c "md result.txt"')
#os.system('cmd c "dir /s new.txt > result.txt"')