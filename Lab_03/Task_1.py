#1)
def for_ounces(grams):
    return 28.3495231 * grams

print(for_ounces(5))


#2)
def from_F_to_C(F):
    return ((5 / 9) * (F - 32))

print(from_F_to_C(45))

#3)
def puzzle(numheads, numlegs):
    for rabbits in range(numheads+1):
        chickens=numheads-rabbits
        if(chickens*2+rabbits*4==numlegs):
            return chickens,rabbits
    return None

numheads = 35
numlegs = 94
result=puzzle(numheads,numlegs)
if result:
    chickens,rabbits=result
    print(f"Chickens: {chickens}, rabbits: {rabbits}")
else:
    print("No solution found.")
    

#4)
def filter_prime(list_num):
    Mylist=list_num.split()
    new_list=[]
    for i in Mylist:
        num=int(i)
        isTrue=0
        for j in range(2,num+1):
            if num%j==0:
                isTrue+=1
        if isTrue<2:
                new_list.append(i)
    print(new_list)


list_1 = "2 3 4 5 6 7 8 9 10 11"
filter_prime(list_1)

#5)
from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")

    perm_list = permutations(user_input)

    for perm in perm_list:
        print(''.join(perm))

print_permutations()

#6)
def reversed_words():
    user_input=input("Enter a string: ")
    word_list= user_input.split()
    result_list=word_list[::-1]
    for i in result_list:
        print(i,end=" ")
    print()

reversed_words()

#7)
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False 

has_33([1, 3, 3]) 
has_33([1, 3, 1, 3])

#8)
def spy_game(nums):
    
    code = [0, 0, 7]

    for num in nums:
        if num == code[0]:
            code.pop(0) 
        if not code:
            return True

    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

#9)
import math
def radius(r):
    print(r**2,"pi^2=",(math.pi*r)**2,sep="")

radius(3)

#10)
def unique_list(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
        

list_2=[1,2,2,3,3,3,4,5,6,7,7]
unique_list(list_2)

#11)
def isSem(str):
    sum_str=len(str)
    rang=0
    if sum_str%2==0:
        rang=int(sum_str/2)
    else:
        rang=int((sum_str-1)/2)
    sum_true=0
    for i in range(rang):
        if str[i]==str[sum_str-1-i]:
            sum_true+=1
    if sum_true==rang:
        print("this is palindrome")
    else:
        print("this is not palindrome")

user_send=input("Send text: ")
isSem(user_send)

#12)
def histogramma(list):
    for i in list:
        repeat=i
        while repeat!=0:
            print("*",end="")
            repeat-=1
        print()


lst_sum=int(input("Sum element: "))
list_3=[]
for i in range(lst_sum):
    list_3.append(int(input("Element: ")))
print(list_3)
histogramma(list_3)

#13)
import random

def rndm_num(name):
    
    num_bot=random.randint(1,20)
    stop_game=False
    sum_Attempt=0
    while stop_game==False:
        num_user=int(input("Take a guess.\n"))
        sum_Attempt+=1
        if num_user==num_bot:
            print(f"Good job, {name}! You guessed my number in {sum_Attempt} guesses!\n")
            stop_game=True
        elif num_user>num_bot:
            print("Your guess is too hight.\n")
        else:
            print("Your guess is too low.\n")


name=input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
rndm_num(name)