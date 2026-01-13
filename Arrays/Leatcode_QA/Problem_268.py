# Problem-268= Find Missing value From the array ( n jitne hai unme se konsa no. list me nhi hai )


# Brute Force 
# Method 1 
# Time and complecxcity = O(n2)=   if not in ka (n) or ek loop ka (n)

num =[1,2,3,0]
# output = 4
n=len(num)

for i in range (0,n+1):
    if i not in num:
        print(i)

#  Better Solution
# Method 2   Using Freq_map(dict())

# time and complexcity = O(3n)= O(n)
# s.c= O(n)   in wrost case of freq_map(dict)

num =[1,2,3,0,5,6,7]
# output = 4
n=len(num)
freq= dict()
for i in range (0,n+1):
    freq[i]=0
for j in num:    
      freq[j]=1
for k in freq:
    if freq[k]==0:
     print(k)      


#  OPTIMAL SOLUTION
# Method 3 Using Formulla (addition of n - sum of (list))
# Time and complexcity = O(n)
num =[1,2,3,0,5,6,4]
# output = 7
n=len(num)

num_addition= n*(n+1)//2
# sum of n 
Final = num_addition - sum(num)


print(Final)
