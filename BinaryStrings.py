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
        else:
            pass
print(count)
print(arr1,arr2)
