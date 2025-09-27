
"""
I create this project to remind everyone that they are loved. I will use the time module
to manage the speed of my message in the output.
"""
import time 

def affection(): 
    affection_text = "I love you" 
    # We want this to run forever hence the 'while True:' in place.
    while True:
        # We create our for loop to better control the timing of each character's upcoming output
        for i in affection_text:   
            print(i, end="") 
            time.sleep(0.2)
        print() # We are now done with the loop and ready to start it over by printing a new line;
            
affection()
