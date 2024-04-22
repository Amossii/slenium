with open('answer.txt','r',encoding='utf-8') as file1:
    with open('utral.txt','w',encoding='utf-8') as file2:
        line=file1.readline()
        while line:
            if '.' not in line:
                file2.write(line)
            else:
                first_char = str(int(line[0]) + 1)
                new_text = first_char + line[1:]
                file2.write(new_text)
            line=file1.readline()
