def sum_letters(text):
    sum_lower_letter = sum(1 for char in text if char.islower())
    sum_upper_letter = sum(1 for char in text if char.isupper())

    print("Sum is lower:",sum_lower_letter)
    print("Sum is upper:",sum_upper_letter)


sum_letters(input("Send text: "))