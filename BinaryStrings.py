
"""Code by M.Shaihu Abdul Kadhir
input format:
first line length of the string..second and third line are the two binary Strings
4      
1101
0011

output
2

the minimum operation required to change string1 and get equals to string2
"""
n=int(input())
str1=input()
str2=input()

count=0

arr1=[]
arr2=[]

def swap(s):
    if(s=='1'):
        s='0'
    else:
        s='1'
    return s

for i in range(n):
    arr1.append(str1[i])
    arr2.append(str2[i])
for i in range(n):
    if(arr1[i]==arr2[i]):
        continue
    else:
        if(arr1[i+1]!=arr2[i+1]):
            if(arr1[i]==arr1[i+1]):
                arr1[i]=swap(arr1[i])
                count=count+1
            else:
                arr1[i]=swap(arr1[i])
                arr1[i+1]=swap(arr1[i+1])
                count=count+1
       
print(count)
print(arr1,arr2)
