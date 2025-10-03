import time # Time module

# vent() function is where most of the magic happens
def vent():
    line1 = "Everyday when I wake up, I feel like a prisoner of my own soul."
    line2 = "I look in the mirror, and the displeasure reaches me."
    line3 = "I just don't want to hate myself any more."
    line4 = "Self-loathing has created this pyroclastic ash cloud inside of my mind."
    line5 = "I just want someone to see me, hear my cries, and show me why I should love myself."
    line6 = "I want to be loved the way I love"
    line7 = "I just want to be ok."

    lines = [line1, line2, line3, line4, line5, line6, line7] # all 7 lines mashed into paragraph

    for line in lines:
        print(line); time.sleep(1.5) # 1 second and a half pause


# Main function
if __name__ == "__main__":
    while True:
        read = input("Read? [Y/N]").strip().upper()
        if read == "Y":
            vent()
        else:
            exit()

