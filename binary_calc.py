
"""
 This project is designed for binary calculations. We can either choose...
 Decimal to Binary
 or...
 Binary to Decimal
 """

# Decimal to Binary
def dec_to_bin():

    # Error handling for dec_to_bin()
    try:
        int_num = int(input("Enter an integer: "))
        bin_result = bin(int_num)[2:] # Base 2 
        print(bin_result) # Our calculation is complete!

        if int_num is not int_num:
            raise ValueError
    except ValueError:
        print("Wrong input. Please enter an integer\n")
        dec_to_bin()

    # Asks the user if they want to use the program again
    use_again1 = input("Use again? [Y/N]\n").strip().upper() 
    if use_again1 != "Y":
        exit()

# Binary to Decimal
def bin_to_dec():
    # Error handling for bin_to_dec()
    try:
        bin_num = input("Enter a binary number: ")
        if bin_num == "0" or "1":
            int_result = int(bin_num, 2) # Calculates from base 2 perspective
            print(int_result) # Our calculation is complete!
        else:
            raise ValueError
    except ValueError:
        print("Wrong input. Please enter a binary number\n")
        bin_to_dec()

    # Asks the user if they want to use the program again
    use_again2 = input("Use again? [Y/N]\n").strip().upper()
    if use_again2 != "Y":
        exit()

# Main function
if __name__ == "__main__":
    print('='*35)
    print("BINARY CALCULATOR")
    print('='*35)

    # Indefinite loop
    while True:
        print("Options:\n[A] Decimal to Binary\n[B] Binary to Decimal")

        # Error handling for the options the user chooses between [A] and [B]
        try:
            user_choice = input("Your selection: ").strip().upper()
            if user_choice == "A":
                dec_to_bin()
            elif user_choice == "B":
                bin_to_dec()
            else:
                raise ValueError
        except ValueError:
            print("That cannot be put. Please choose either [A] or [B]\n")




        
