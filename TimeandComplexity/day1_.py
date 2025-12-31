# linear search o(n)
def search_num(arr, target):
 for i in range(len(arr)):
    if arr[i] == target :
      return i
    

 return -1
    
my_list= [10, 20, 30, 40, 50]  
number_targeet= 40 
print (search_num(my_list,number_targeet))     

