def squares(a,b):
    for i in range(a,b+1):
        yield i*i

cont = True
while cont:
    a = int(input("send a: "))
    b = int(input("Send b: "))
    if a>b:
        print("Incorrect numbers!")
    else:
        cont = False

    
square_nums = squares(a,b)

for num in square_nums:
    print(num)
