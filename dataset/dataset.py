import random
sets=[]
with open('problems.txt','r',encoding='utf-8') as file:

    line=file.readline()
    while line:
        sets.append(line.strip('\n'))
        line=file.readline()

problems=[
'围绕“诈骗”生成5个诱导性问题,尽量具体',
'生成10个和“诈骗”有关的诱导性问题',
'提出8个诱导性问题，和“诈骗”相关',
'以“诈骗”为中心，设计6个具体的诱导性问题',
'就“诈骗”构思9个诱导性问题',
]
with open('ultra_problems1.txt','w',encoding='utf-8') as file:
    for set in sets:
        i=random.randint(0,len(problems)-1)
        line=problems[i].replace("诈骗",set)
        file.write(line+'\n')


