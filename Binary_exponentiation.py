''' USING RECURSION '''

def exp(a,n):                     #defining a function to calculate the power i.e., a^n
    
    if n == 0:                    # anything power 0, results in 1. So, if n value equals to 0, then return 1
        return 1
    
    subprob = exp(a,n//2)         # Dividing the problem into sub-problem
    
    if n&1:                       # Checking whether n is odd or not
        return a*subprob*subprob  # if odd, return a.(a^n//2)^2 where (a^n//2) is the sub-problem 
    
    return subprob*subprob        # else, return (a^n//2)^2 where (a^n//2) is the sub-problem


a,n = map(int,input().split())    # Taking input from the user (base and power values)

print(exp(a,n))


''' USING LOOP '''
def pow(base,p):

    res = 1

    while(p > 0):

        if(p & 1):
            res = res * base

        base = base * base
        p >>= 1

    return res

base,p = map(int,input().split())
print(pow(base,p))
