import datetime
import os
import time

for i in range (10):
    now = datetime.datetime.now()
    name = 'raport.txt'
    my_now = now.strftime('%H%M%S')
    print(name[:5] + my_now + name[-4:])
    time.sleep(2)
#os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop\\. && dir /s new.txt >> result.txt"')