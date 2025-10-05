# I will import time for the speed of the program and sys to make modifications to how text is written directly to terminal should run it
import time 
import sys 

# vent() function is where most of the magic happens
def vent():

    # This function will determine the text speed to be 0.1 miliseconds.
    def text_speed(text,delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush() # Characters will be processed immediately
            time.sleep(delay)

    lines = ["Everyday when I wake up, I feel like a prisoner of my own soul.\n", 
            "I look in the mirror, and the displeasure reaches me.\n",
             "I just don't want to hate myself any more.\n", 
             "Self-loathing has created this pyroclastic ash cloud inside of my mind.\n",
             "I just want someone to see me, hear my cries, and show me why I should love myself.\n",
             "I want to be loved the way I love\n", 
             "I just want to be ok.\n"]
    # Sentences
    

    for line in lines:
        text_speed(line)


# Main function
if __name__ == "__main__":
    while True:
        read = input("Read? [Y/N]").strip().upper()
        if read == "Y":
            vent()
        else:
            exit()

