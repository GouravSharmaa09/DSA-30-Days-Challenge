# theory -1   Head Recursion  without parameterized  [in head recursion first we done a jon (print) then call a fun()]
#output = number btao bro tuje recursion dikhau :6
# gourav
# gourav
# gourav
# gourav
# gourav
# gourav

count = 0 
num = int(input("number btao bro tuje recursion dikhau :"))
def fun():
    global count
    if count == num:
      return
    print("gourav")
    count+=1
    fun()    
fun()


# 2. Tail Recursion [ fun call first then jo b reverse of head ] 
count= 0
def fun():
    global count 
    if count == 4 :
        return 
    print ("Gourav Sharma")
    count+=1
    fun()
fun()        
    


# Problem 1= Recursion using parameter 
# output = Yo Yo Honey Singh
# Yo Yo Honey Singh
# Yo Yo Honey Singh
# Yo Yo Honey Singh
# Yo Yo Honey Singh     
# Time complexcity = O(n)
# Space complexcity = O (n)
def gourav(x, n):
    if n ==0:
        return
    print(x)
    gourav(x,n-1)
gourav("Yo Yo Honey Singh",5)        



# Problem - 2   Print 1 to n  using Recursion so we can solve it Tail recursion 
# # output= Dhurandhar 2026  : Bade Shaab ....?
# 1
# Dhurandhar 2026  : Bade Shaab ....?
# 2
# Dhurandhar 2026  : Bade Shaab ....?
# 3
# Dhurandhar 2026  : Bade Shaab ....?
# 4
# Dhurandhar 2026  : Bade Shaab ....?
# 5
# Dhurandhar 2026  : Bade Shaab ....?
# 6
# Dhurandhar 2026  : Bade Shaab ....?
# 7
# Dhurandhar 2026  : Bade Shaab ....?
# 8
# Dhurandhar 2026  : Bade Shaab ....?
# 9
# Dhurandhar 2026  : Bade Shaab ....?
# 10
# Time complexcity and space complexcity = O(n)

def gourav(n):
    if n ==0:
        return 
    gourav(n-1)
    print("Dhurandhar 2026  : Bade Shaab ....?")
    print(n)
gourav(10)        







# Print 1 to n using Head recursion 
# output= 1
# 2
# 3
# 4
# 5
# 6

def gourav(i, n):
    if n<i :
        return 
    print(i)
    gourav(i+1,n)
gourav(1,6)       



#  Parameterized / Functional Recursion 
# Problem 5 =  Sum of 1 to N [parameterized]
# output = 15

def gourav(sum, i , n ):
    if n<i :
        print ( sum )
        # agr i jyda hai n se to sum print kro  else retrun kro 
        return
    gourav(sum+i,i+1,n)
gourav(0,1,5)    




# Problem = 6 Sum of 1 to N using Functional

def gourav (n):
     if n == 1:
        return 1
     return n+gourav(n-1)
print(gourav(5))     

