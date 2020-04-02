import math
from collections import Counter

N=int(input())


x=list(map(int,input().split()[:N]))
print(x)
length=len(x)

def odd_even(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

#print(x,length)

#sum_list=sum(x)
#print(sum_list)
def mean(value,size):

    return round(sum(value)/size,1)

def median(values):
    values.sort()
    l=len(values)
  
    check_bit=odd_even(l)
    if(check_bit==1):
        index=int(l/2)
        return  round((values[index-1]+values[index])/2,1)
       # print(values[index-1])
        #print(values[index])
     
    else:
        index=int(l/2)
        return values[index]
        #print(values[index])

def mode(values):
    values.sort()
    my_dict=Counter(values)
    
    Keymax = max(my_dict, key=my_dict.get) 
    return Keymax

print("Mean",mean(x,length))
print("Median",median(x))
print("Mode",mode(x))
        

