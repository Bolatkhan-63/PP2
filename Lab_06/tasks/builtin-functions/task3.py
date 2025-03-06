def is_palindrome(word):
    word = word.lower()
    sym = "".join(reversed(word)) #word[::-1]
    if word==sym:
        print("This word is palindrome")
    else:
        print("This word is not palindrome")

word = input("Send word: ")
is_palindrome(word)