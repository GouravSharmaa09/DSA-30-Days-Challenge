# Problem = Merge the Two sorted Array Along no Duplicate in the array 
# output = [1, 2, 3, 4, 5, 6, 7, 8]
# Time complexcity = o(n+m)

num_1= [1,1,1,2,4,5,6,7,7]
num_2 = [1,2,3,6,7,8,8]
m,n= len(num_1),len(num_2)
i,j=0,0
result=[]
while i<m and j<n:
#  condition checking for like list me len se jyda items hai ky nhi 
    if num_1[i]< num_2[j]:
        #  num1 less than hai num 2 se to 
        if len(result)==0 or result[-1]!= num_1[i]:
        #    ye duplicates ko remove krne ke liye ki elements ko khali list me daalte hai -1 to vo num ke equal to nhi for checking 
            result.append (num_1[i])
        i+=1
    elif num_2[j]<num_1[i]:
        #  num 2 less than hai num i se to 
        if len(result)==0 or result[-1]!= num_2[j]:
#             
              result.append(num_2[j])
        j+=1
    elif num_1[i]==num_2[j]:
        #  both equal then also chk for duplicates 
        if len(result)==0 or result[-1]!= num_1[i]:
              result.append(num_1[i])
        i+=1
        j+=1
while i<m:
    #  remaining elements in the lists 
    if len(result)==0 or result[-1]!= num_1[i]:
              result.append(num_1[i])
    i+=1

while j<n:
    if len(result)==0 or result[-1]!= num_2[j]:
               result.append(num_2[j])
    j+=1    
print(result)            










