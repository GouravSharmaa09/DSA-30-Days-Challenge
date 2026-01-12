# Problem = Rotate Array by one place ( change only done in Array) 
# 1---- Using Slicing 

num=[1,-2,3,4,5,6,7,8,9]

# ouput = [9, 1, -2, 3, 4, 5, 6, 7, 8]

n=len(num)

num[:]= num[n-1:]+ num[0:n-1]
#  slicing Time complexcity = O(n)   (  first vala var me slicing :  isliye hai kyuki change only arr me krna hai and n-1: vala push krne ke liye last elelment in first )

print(num)





# 2.1 ------- Using Without Slicing 
# Time complexcity = O(n)

num=[1,-2,3,4,5,6,7,8,9,0,2,3]

# output = [3, 1, -2, 3, 4, 5, 6, 7, 8, 9, 0, 2]

n=len(num)

store= num[n-1]
#  variable me last vale ki value store krli 

for i in range (n-2,-1,-1):
    #  loop iterate kiya second last element se or every time i+1 kiya 
    num[i+1]=num[i]
num[0]= store
print(num)



# 3.1 ----- using Push and pop(insert or pop)

num=[1,-2,3,4,5,6]
# output= [6, 1, -2, 3, 4, 5]
n=len(num)

last_element= num.pop()
#  pop the last elemnt in the arr 

num.insert(0,last_element)
#  insert at 0 index 

print(num)





