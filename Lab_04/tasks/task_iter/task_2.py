def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n = int(input("Send N: "))

nums = even_numbers(n)

print(",".join(map(str, nums)))
