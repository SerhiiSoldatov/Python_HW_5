# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
with open('Task1file1.txt','r',encoding='utf-8') as file: 
    text1=file.readline()
with open('Task1file2.txt','r',encoding='utf-8') as file: 
    text2=file.readline()
def search (text1,text2):
    separ=[' ',',','.','!',';',':','?']
    index1=0
    index2=0
    for i in range(0,len(text1)+1):
        if text1[i:i+len(text2)]==text2:
            for k in range(i,0,-1):
                if text1[k]==' ':
                    index1=k+1
                    break
            for j in range(i,len(text1)+1):
                if text1[j] in separ:
                    index2=j
                    break
            text1=text1[:index1]+' '*(index2-index1)+text1[index2:]#я заменил пробелами
            # удаленные слова, для лучшего восприятия результата
    return text1      
print(text1)
print(search(text1,text2))
with open('Task1file3.txt','w',encoding='utf-8') as file: 
    file.write(f'{text1}\n')
    file.write(f'{search(text1,text2)}')