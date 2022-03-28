#PROGRAM-1 MULTIPLES OF 3 AND 5

num = int(input())

x=0

for i in range(num):
    
    if i%3==0 or i%5==0:
        
            x+=i
            
print(x)


#PROGRAM-2 EVEN VAL SUM FIB SERIES

n=1
a=2
l=[]
while(n<400000):
    