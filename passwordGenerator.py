import random

# Gets input from user the length of password to be generated.
length = int(input("Enter the length of password to be generated: "))

if (length > 72):
    print("The length of password cannot be more than 72.")

else:
    # collection of lower cases.
    lower = "abcdefghijklmnopqrstuvwxyz"

    # collection of upper cases.
    upper = lower.upper()

    # collection of numbers.
    numb = "1234567890"

    # collection of symbols.
    symbols = "!@#$%^&*()"

    # concatenation of lower, upper, numb and symbols.
    string = lower + upper + numb + symbols

    # The join(iterable) function takes all items in an iterable and joins them into one string.
    # The sample(sequence, length) function returns a list with a randomly selection of a specified number of items from a sequnce.
    print(f"Generated password is: \n{''.join(random.sample(string, length))}")
