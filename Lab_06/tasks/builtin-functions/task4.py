import math
import time

def find_square(n,t):
    s = t/1000
    time.sleep(s)
    square = math.sqrt(n)

    print(f"Square root of {square} after {t} miliseconds is {square}")

n = int(input("Send N: "))
t = int(input("Send T: "))
find_square(n,t)
    