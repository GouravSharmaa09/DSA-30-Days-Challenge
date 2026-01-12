# Problem = Remove the duplicates from the array and count the unique number in its accourding to manner

# 1.1--- using freq_map
# Time and complexcity= O(2n)= o(n)
# space .complexcity= o(1)

num=[1,1,1,2,2,3,3,4,4,5,6,7,7,7,7,8,9]
# output = 9
n=len(num)
freq_map= dict()

for i in range (0,n):
    freq_map[num[i]]=0
j=0
for k in freq_map:
    num[j]=k
    j+=1
print(j)    



#  1.2 --- Using Two Pointer 

num=[1,1,1,2,2,3,3,4,4,5,6,7,7,7,7,8,9]
n=len(num)
i=0
j=i+1
while j<n:
    if num[j]!= num[i]:
        i+=1
        num[i],num[j]=num[j],num[i]
    j+=1
print(i+1)        

