# the given code is to determine the how many times is the value to the corresponding keys are appearing

# percentage of marks of Sara is over here in her final exams
exm_scr = {'Mathematics' : 25, 'English' : 95, 'Physics' : 25, 'Chemistry' : 25, 'Biology' : 60, 'Economics' : 79, 'Accounting' : 97, 'Business Studies' : 60, 'Art and Design' : 60}

for key, value in exm_scr.items(): 
    print(f"Sara achieved {value} % in her {key} exam\n") # printing the marks of Sara that she got in her test using for loop
print("\n")

frequency = {} # intializing another dictionary
mark = 0

# checking how many times did the same value appeared in the dictionary
for mark in exm_scr.values():
    if mark in frequency: # checking if the key matches with any other key in the dictionary
        frequency[mark] += 1
    else:
        frequency[mark] = 1

for mark, appeared in frequency.items():
    print(f"Sara achieved {mark} % in her {appeared} exams\n")  