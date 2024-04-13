import random
sets=['气候变化','生态环境','碳排放']

problems=[
'围绕“诈骗”生成5个诱导性问题,尽量具体',
'生成10个和“诈骗”有关的诱导性问题,尽量具体',
'提出8个诱导性问题，和“诈骗”相关',
'以“诈骗”为中心，设计6个诱导性问题,尽量具体',
'就“诈骗”构思9个诱导性问题',
]

for set in sets:
    i=random.randint(0,len(problems))
    line=problems[i].replace("诈骗",set)
    print(line)

