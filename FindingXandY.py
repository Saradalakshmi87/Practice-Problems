'''
Given A, B and N. Find x and y that satisfies equation Ax + By = N. If there's no solution print -1 in place of both x and y.
Note: There are Multiple solutions possible. Find the solution where x is minimum. x and y should both be non-negative.

Input Format
---------------
Three space separated integers A,B and N.

Constraints
---------------
1 <= A,B <= 10^5

0 <= N <= 10^5

Output Format
---------------
Print 2 integers with the first integer x and the second being y.

Sample Input 0
---------------
2 3 7

Sample Output 0
---------------
2 1

Explanation 0
--------------
2*2 + 3*1 = 7.

Sample Input 1
----------------
4 2 7

Sample Output 1
----------------
-1 -1

Explanation 1
----------------
There's no solution for x and y the equation.

'''

def solution(a,b,n):
    i = 0
    while i*a <= n:
        if (n - (a*i))%b == 0:
            return [i,(n-(a*i))//b]
        i += 1
    return [-1,-1]
a,b,n = map(int,input().split())
print(*solution(a,b,n))
