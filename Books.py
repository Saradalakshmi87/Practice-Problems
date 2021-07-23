'''
When Valera has got some free time, he goes to the library to read some books. Today he's got t free minutes to read.
That's why Valera took n books in the library and for each book he estimated the time he is going to need to read it.
Let's number the books by integers from 1 to n. Valera needs ai minutes to read the i-th book.

Valera decided to choose an arbitrary book with number i and read the books one by one, starting from this book.
In other words, he will first read book number i, then book number i + 1, then book number i + 2 and so on.
He continues the process until he either runs out of the free time or finishes reading the n-th book.
Valera reads each book up to the end, that is, he doesn't start reading the book if he doesn't have enough free time to finish reading it.

Print the maximum number of books Valera can read.

Input Format:
------------------

The first line contains two integers n and t — the number of books and the number of free minutes Valera's got. The second line contains a sequence of n integers a1, a2, ..., an, where number ai shows the number of minutes that the boy needs to read the i-th book.

Constraints

(1 ≤ n ≤ 10^5; 1 ≤ t ≤ 10^9)

(1 ≤ ai ≤ 10^4)

Output Format:
------------------

Print a single integer — the maximum number of books Valera can read.

Sample Input 0:
------------------

4 5
3 1 2 1

Sample Output 0:
------------------

3

Sample Input 1
-----------------

3 3
2 2 3

Sample Output 1
-----------------

1

'''


#CODE

m,t = map(int,input().split())
a = [int(i) for i in input().split()][:m]
s,c = 0,0
for i in a:
    s += i
    if s <= t:
        c += 1
    elif s > t:
        s -= i
print(c)
