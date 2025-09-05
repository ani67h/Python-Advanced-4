import random

alphabets = "qwertyuiopasdfghjklzxcvbnm"
special_charec = "!@#$%^&*()_{}[]':;.,"
relations = "-=+<>/*" 

ran_char = alphabets + relations + special_charec    

ran_pass = ""
for i in range(12):
    ran_pass += random.choice(ran_char)  

print("Your password is ",ran_pass)