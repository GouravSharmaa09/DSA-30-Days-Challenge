# Problem-2149=  Rearrange the array by the sign of elements 

# 1- Brute force 

# Time complexcity = O(n+n/2)= O(n)

num = [5,10,-3,-1,-10,6]
# output = [5, -3, 10, -1, 6, -10]

n=len(num)
pos=[]
#  do list bnayi pos or neg ke liye but chnages num ke andr hi krege 
neg=[]

for i in range (n):
    #  iterate until len n 
    if num [i]>0:
        #  num 0 se bda hai to vlaue pos me daalo else neg me 
      pos.append(num[i])
    else:
        neg.append(num[i])  
for j in range (len(pos)):
    #  iterate on len(pos ) or agr chaye to neg pe bhi krva skte hai 

    num[2*j]= pos[j]
    #  logic -- 2*j = positive or +1 krgee to negative ind pe (2*0=0) to 0 index pe positive or +1 krege to 1 to 1 pe negative 
    num[2*j+1]= neg[j]
print(num)        







# Method 2 -- Optimal Using Two pointer 

# time and complexicty = O(N)  AND S.C IN WROST CASE = O(N)

num=[5,10,-3,-4,-8,7]
# output = [5, -3, 10, -4, 7, -8]  
n=len(num)
# pos_index = 0 or negative 1  
pos_ind,neg_ind= 0,1
#  result arr me 0 intilize krna hai starting me 
result=[0]*n

for i in range (0,n):

    if num[i]>0:
        result[pos_ind]=num[i]
        #  result pos_ind 0 pr num i ki valueset kro  
        pos_ind+=2
        #  or pos_ind ko 2 increment kro and same vo neagtive but 0 se km ho to 
    else:
        result[neg_ind]=num[i]
        neg_ind+=2
print(result)            
