"""we are counting the frequency of same value, how mant times it is appearing for different key"""
# Initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 2

# Using loop
# Selective key values in dictionary
result = 0
for key in test_dict:
    if test_dict[key] == K:
        result = result + 1

# printing result
print("Frequency of K is : " + str(result))     