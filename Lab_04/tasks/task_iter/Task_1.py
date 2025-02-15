def square_number(n):
    for i in range(1,n+1):
        yield (i*i)

N = int(input("Send N: "))

nums=square_number(N)

for i in range(N):
    print(next(nums))
    

