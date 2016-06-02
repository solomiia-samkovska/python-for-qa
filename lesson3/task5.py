import os

i = 1
os.mkdir("d:/python-for-qa")
while i <= 5:
    os.mkdir("d:/python-for-qa/lesson" + str(i))
    n = 1
    while n <= 6:
        f = open("d:/python-for-qa/lesson" + str(i) + '/task' + str(n) + '.py', 'w')
        n = n + 1
    i = i + 1


