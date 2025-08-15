# add tow lists using map and lambda
number1 = [1,2,3]
number2 = [4,5,6]
result = map(lambda x,y: x + y, number1, number2)
print("Addition of two list : ")
print(list(result))

# using map
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,nums)) # map is used to apply a function
print("Square of numbers in lists : ")
print(square)