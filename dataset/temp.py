# 打开文件（默认以只读模式打开）
import random
sets=[]
with open('keywords.txt', 'r',encoding='utf-8') as file:
    # 读取文件内容
    line=file.readline()
    while line:
        sets.append(line.strip('\n'))
        line=file.readline()
with open('problems.txt','w',encoding='utf-8') as file:
    for i in range(6):
        t=random.randint(0,10)
        for j in range(1+t,11+t):
            index=22*i+j
            text=sets[index].split(' ')[1]
            file.write(text+'\n')
            print(text)
