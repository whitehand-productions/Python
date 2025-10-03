import time # Time module

# vent() function is where most of the magic happens
def vent():
    lines = ["Everyday when I wake up, I feel like a prisoner of my own soul.", 
            "I look in the mirror, and the displeasure reaches me.",
             "I just don't want to hate myself any more.", 
             "Self-loathing has created this pyroclastic ash cloud inside of my mind.",
             "I just want someone to see me, hear my cries, and show me why I should love myself.",
             "I want to be loved the way I love", 
             "I just want to be ok."]
    

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


