def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)
n=0
sum=0
while True:
    n+=1
    fib = fibo(n)
    if fib%2==0:
        sum+=fib
    if fib > 4000000:
        break
print(sum)