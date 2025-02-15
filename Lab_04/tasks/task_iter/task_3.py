def func3(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n = int(input("Send N: "))

nums = func3(n)

print(" ".join(map(str, nums)))