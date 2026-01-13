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




#  Using Reverse Array   Time complexcity = O(n2) and s.c = O(1)
# output = [5, -2, 6, 5, 4, 3, 9]
# [4, 3, 9, 5, -2, 6, 5]
# [6, 5, 4, 3, 9, 5, -2]

def reverse(arr,left,right):
     
# num =[3,9,5,-2,6,5,4]
      while left<right :
        #  agr left chota hai right se to swap it 
        arr[left],arr[right]= arr[right],arr[left]
        left+=1
        #  increment left and decrease right at one step every time 
        right-=1
arr=[3,9,5,-2,6,5,4]    
n=len(arr)
k= 3
k=k%n
reverse(arr,n-k,n-1)  
#  k index tk ki list ko swap ke liye    O(k/2)
reverse(arr,0,n-k-1)
#  bche huye element ko reverse krege   O(n-k)/2
reverse(arr,0,n-1)  
#  Full arry ko reverse kro  O(n/2)

# Total = O(k/2 + n-k/2 + n/2) =  O(n2)

print(arr)
