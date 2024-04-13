# 打开文件（默认以只读模式打开）
import random
sets=[]
with open('keywords.txt', 'r',encoding='utf-8') as file:
    # 读取文件内容
    line=file.readline().strip('\n')
    while line:
        sets.append(line)
        line=file.readline().strip('\n')

for i in range(6):
    t=random.randint(0,10)

    for j in range(1+t,11+t):
        index=22*i+j
        print(sets[j])
