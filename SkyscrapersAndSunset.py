'''
Das lives in a city which is having skyscrapers. Das has a wish and wants to see the buildings on which sunlight falls when the sun sets.
Help him in counting the number of buildings receiving the sunlight. Note: A taller building casts a shadow on a shorter building.
Given an array H denoting heights of buildings. You have to count the buildings which will see the sun set
(Assume : Sun set on the side of array ending i.e at the last element of the array).

It is given that all buildings are of different height.

Input Format
-------------
The first line of N, N is the number of buildings. The second line of contains separated values of heights of buildings.

Constraints
-------------
1 ≤ N ≤ 10^6 1 ≤ Hi ≤ 10^8

Output Format
-------------
Print the total number of buildings which will see the sunset.

Sample Input 0
--------------
5
7 4 8 2 9

Sample Output 0
---------------
1

Sample Input 1
---------------
4
5 3 4 1

Sample Output 1
---------------
3

'''

#CODE
n = int(input())
l = [int(i) for i in input().split()][:n][::-1]
c = 1
m = l[0]
for i in range(n):
    if l[i] > m:
        c += 1
        m = l[i]
print(c)
