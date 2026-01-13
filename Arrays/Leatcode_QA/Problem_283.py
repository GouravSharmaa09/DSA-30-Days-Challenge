# Problem 283 = Move Zeros at the end of array but in the same sequnece remain of numbers in it 
# output = [1, 2, 4, 3, 3, 5, 1, 0, 0, 0]
# Time_complexcity = O(n)

num= [1,0,2,4,3,0,0,3,5,1]
n=len(num)
i=0
#  intitial me i or j both 0 rhege , agr j ko zero mila to vo usko i se swap krega and i +=1 hota rhega 
for j in range (n):
    if num[j]!= 0:
        num[i],num[j]=num[j],num[i]
        i+=1
print(num)                



 