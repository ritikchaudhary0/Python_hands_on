#Given a number N, print sum of all even numbers from 1 to N.

n = int(input())

start_n = 1
sum = 0


while start_n <= n:
    if start_n%2 == 0:
        sum = sum + start_n
    start_n = start_n+1
    
print(sum)
