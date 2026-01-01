# pattern 1
# *****
# *****
# *****
# *****
# *****


for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print("")    


# Pattern =2 
# *
# **
# ***
# ****
# *****


for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print("")    

# pattern= 3
# 1
# 12
# 123
# 1234
# 12345


for i in range (1,6):
    for j in range(1,i+1):
        print (j, end="")
    print("")    


# pattern = 4 
# 1
# 22
# 333
# 4444
# 55555  



for i in range (1,6):
    for j in range(i):
        print (i, end="")
    print("")   


# pattern = 5
# *****
# ****
# ***
# **
# *


for i in range (1,6):
    for j in range(6,i,-1):
        print ("*",end="")
    print("")



# Pattern = 6
#     * 
#    *** 
#   ***** 
#  ******* 
# *********
# in this we use (space) , print(star), then again no need beacuse bd me space lene ka mtlb nhi * ke bd me next line ke liye jo print"" krvate hai usko innerloop ke bhar likh do right space automatically bn jyega kyuki next line se hoga agla star ka km 
# for space loop ke liye formula (n - i) kyuki n= (no. of rows i) i increase hone pe space decrease hoga   
# for star loop formula is 2*i-1 beacause hmesha odd no. aayege star ke liye 2*1 - 1 = 1 for 1 row of pyramid 


for i in range(1,6):
    
    for j in range (6-i):    
        print(" ", end="")
    
    for j in range (2*i - 1):
        print("*", end="")
    
    print("")   



# pattern = 7
# 12345
# 1234
# 123
# 12
# 1





for i in range (5,0,-1):
    
    for j in range (1,i+1):
    
        print(j,end="")
    
    print("")        
      
    