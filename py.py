import os
i=0
while True:
    
    #write

    f = open('test0.txt', 'a')
    f.write(".")

    #Add
    os.system('git add .')
    os.system('git commit -m "1"')
    os.system('git push origin master')
    i=i+1
    print(str(i)+':commits')
