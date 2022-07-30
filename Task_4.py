# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
import re
with open('Task4file1.txt','r',encoding='utf-8') as file: 
    strokaStart=file.readline()
strokaFinish=''
spisokStart=[]
spisokFinish=[]
tempSymbol=''
tempString=''
counter=''
i=0
k=0
while i<len(strokaStart):
    tempSymbol=strokaStart[i]
    j=i
    while j<len(strokaStart):
        if tempSymbol not in strokaStart[j]:
            tempString=strokaStart[i:j]
            counter=str(tempString.count(tempSymbol))
            strokaFinish=strokaFinish+counter+tempSymbol
            k=j
            j=len(strokaStart)
        elif j==len(strokaStart)-1:
            strokaFinish=strokaFinish+str(j-i+1)+tempSymbol
            k=j+1
            break            
        else:            
            j+=1
    i=k
print(strokaStart)
print(strokaFinish)
with open('Task4file2.txt','w',encoding='utf-8') as file: 
    file.write(f'{strokaFinish}\n')
strokaStart=''
strokaFinish=''
with open('Task4file2.txt','r',encoding='utf-8') as file: 
    strokaStart=file.readline()
print(strokaStart)
spisokKoff=re.findall('\d+', strokaStart)
i=0
k=0
while i<len(strokaStart)-1:
    if strokaStart[i].isdigit():
        i+=1
    else:
        strokaFinish=strokaFinish+strokaStart[i]*int(spisokKoff[k])
        i+=1
        k+=1 
print(strokaFinish)