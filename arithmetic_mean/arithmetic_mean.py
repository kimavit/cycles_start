a=int (input())
b=int (input())
sum = 0
count = 0
for i in range (a,b+1):
    if i%3==0:
        sum +=1
        count +=i
print (count/sum)