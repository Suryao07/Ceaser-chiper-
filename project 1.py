def generate(x):
    a = list(x)
    code_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        changed = [(code_list[(code_list.index(char) + 3) % 26]) for char in a]
        result = ''.join(changed)
        print("Generated Code:", result)
    except ValueError:
        print("Invalid input... Only alphabets are allowed.")

def decode(y):
    a = list(y)
    code_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        changed = [(code_list[(code_list.index(char) - 3) % 26]) for char in a]
        result = ''.join(changed)
        print("Decoded Message:", result)
    except ValueError:
        print("Invalid input... Only alphabets are allowed.")

print("Hello Welcome \n<< CAESAR CIPHER CODE >>")
while True:
    print("\nMENU \n1. Generate \n2. Decode \n3. Exit")
    ch = int(input("Enter Your choice: "))

    if ch == 1:
        input1 = input("Enter the word to generate code: ")
        input2 = input1.upper()
        generate(input2)
    elif ch == 2:
        input3 = input("Enter the Caesar Cipher code to decode: ")
        input4 = input3.upper()
        decode(input4)
    elif ch == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")