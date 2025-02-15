def inverse_numbers(n):
    for i in range(n,-1,-1):
        yield i

n = int(input("Send N: "))

nums = inverse_numbers(n)

for num in nums:
    print(num)