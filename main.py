# Josh Daniels
def menu():
    print("Menu")
    print("-----------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encoder(password):
    encoded_password = ''
    for i in range(len(password)):
        encoded = str(int(password[i]) + 3)
        encoded_password += encoded
    return encoded_password

#Nicholas Borden
def decoder(password):
    decoded_password = ''
    for i in range(len(password)):
        encoded = str(int(password[i]) - 3)
        decoded_password += encoded
    return decoded_password

while True:
    menu()
    choice = int(input('Please enter an option: '))
    if choice == 1:
        password1 = input('Please enter your password to encode:')
        encoded_final = encoder(password1)
        print('Your password has been encoded!')
    if choice == 2:
        decoded_password = decoder(encoded_final)
        print("The encoded password is " + encoded_final + ", and the original password is " + decoded_password + ".\n")
    if choice == 3:
        exit()
