




print("--- Welcome to Binary Calculator --- ")
running = True

def dec_to_bin():
    input_num = int("Please enter a number: ")
    bin_conversion = bin(input_num)[2:]
    print(bin_conversion)

def bin_to_dec():
    input_bin = int("Please enter a binary number: ")
    int_result = bin(input_bin)
    int_result = int(input_bin)

while running:

    try:
        user_choice = input("[A] Binary to Decimal\n[B] Decimal to Binary\nYour response: ")
        if user_choice.upper() == "A":
            dec_to_bin()
        elif user_choice.upper() == "B":
            bin_to_dec()
        else:
            raise ValueError
    except ValueError:
        print("Wrong Input\n")

        


        