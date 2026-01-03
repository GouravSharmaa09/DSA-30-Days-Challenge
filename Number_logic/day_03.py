#  ARMSTRONG NUMBER LOGIC PROBLEM 
# PROBLEM 1 
# digit count and sum ka logic 
#  using floor division or reminder logic  we calcualte length or sum or input

n = 5432
num = n 
count=0
total_sum=0
while num > 0 :
  count+=1  
  last_digit = num%10 
  total_sum= total_sum+(last_digit)
  num= num//10
print(total_sum)
print(count)




# PROBLEM - 2  ARMSTRONG+ CUBE+ADDITION 
# the code take an input and accourding the input give the solx are the vaild cube or not but it also check the sum of input number are equal to cube then only shows a vaild cube else not vaild 


number= int(input("bhai number bta bhi de :"))
num_og=number
total= 0
while num_og > 0 :
    last_digit = num_og%10
    total = total+(last_digit**3)
    num_og = num_og//10
if total ==number :
        print ("vaild cube" ,total)
elif total != num_og:
        print("not a vaild cube" ,total)