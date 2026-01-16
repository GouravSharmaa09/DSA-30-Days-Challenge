# Problem - 121 = Stock Buy And Sell  
# In the array find the maximum profit stock 
# Method 1 - Brute Force  USING TWO POINTER

# Time and complexcity = O(n(n+1)/2)= O(n^2)

num= [7,2,1,5,6,4,8]
# output= 7
n = len(num)
maximum_profit=0

for i in range (0,n):
    for j in range (i+1,n):
        if num[j]>num[i]:
            #  AGR J chota hai i se to minmum price nikalo 
            min_price= num[j]-num[i]
            #  maximum profit ke liye 
            maximum_profit= max(maximum_profit,min_price)
print(maximum_profit)





# OPTIMAL SOLUTION -- USING KADANE'S ALGORITHM 

# TIME AND COMPLEXCITY = 0(n) 

price=[7,2,1,5,6,4,8,9,10,]
# output= 9
#  
n=len(price)
min_price= float("inf")
#  sbse bdi value li hai infinite 
maximum_profit= 0

for i in range (0,n):
    min_price= min(min_price,price[i])
    #  loopfirst chlte hi min_price check krege agr min price[i] se km hai to min ko update krege vrna nhi 
    
    current_profit= price[i]-min_price
    #  current profit btyega price[i] or min ka diff

    maximum_profit= max(maximum_profit,current_profit)
    #  max profit 
print(maximum_profit)    




