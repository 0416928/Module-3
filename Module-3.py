'''
Module-03
'''

# Code example of control structures
'''
number = 0
# a boolean expression is anything that evalutaes to true or false
print(f"Number = {number}")
if number > 0:
    print("Number is positive")
    print("This is a second line of output")

elif number == 0:
    print("Number is zero")

else:
    print("Number is negative")


# Indentation matters
number = 3
if number == 1:
   print("Number is 1")
   print("Line 25")
elif number == 2:
   print("Number is 2")
   print("Line 28")

elif number == 3:
   print("Number is 3")
   print("Line 32")

elif number == 4:
   print("Number is 4")
   print("Line 36")

elif number == 5:
   print("Number is 5")
   print("Line 40")

print("End of if")


# Challenge
number = 20
if number == 15:
   print("True")
else:
   print("False")


age = 18
if age < 13:
  print("Child")
elif age < 18:
  print("Teenager")
else:
  print("Adult")
# Output Adult


horizontal_position = 3
vertical_position = 5

# Use nested if-else statements to determine the quadrant of the position
if horizontal_position > 0:
    if vertical_position > 0:
        print("Both horizontal_position and vertical_position are positive")
    else:
        print("horizontal_position is positive, but vertical_position is not")
else:
    if vertical_position > 0:
        print("vertical_position is positive, but horizontal_position is not")
    else:
        print("Both horizontal_position and vertical_position are not positive")

# Output: Both horizontal_position and vertical_position are positive

'''
# Boolean variable 
is_sunny = False
print(f"is_sunny = {is_sunny}")

if is_sunny:
    print("It is a sunny day!")
else:
    print("It is a rainy day!")



grade = 51
print(f"Grade = {grade}")
if grade >= 50:
  print("You pass")
elif grade < 50:
  print("You fail")


my_age = 5
friends_age = 10

# and / or / not

if not my_age >10:
   print("True...")
if my_age == 0 and friends_age ==0:
   print("Using and logic ")





# # Loops
# number =1 
# for number in range(10):
#   print(number)
