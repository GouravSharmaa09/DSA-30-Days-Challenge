# Problem - 189  -- Rotate Array by K place 

# using ----- Push/pop
# Time_complexcity= O(R*n)

num =[3,9,5,-2,6,5,4]
#  output = [5, -2, 6, 5, 4, 3, 9]
n=len(num)
k=5
Operation=k%n
for i in range (0,k):
    e= num.pop()
    num.insert(0,e)


print(num)    


# Using Slicing 

# time complexcity= O(K+N-K)= O(N) 
num =[3,9,5,-2,6,5,4]
# ouptu = [4, 3, 9, 5, -2, 6, 5] 
k=3
k=n%k

num[:]= num[n-k:]+ num[:n-k]

print(num)
