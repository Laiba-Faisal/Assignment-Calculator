# 1. Simple Message
sms = "August 14 is Independence Day of Pakistan."
print(sms)

# 2. Simple Messages
message = "I live in Lahore city."
print(message)
print("")  # Just to separate the messages

# Changing the value of a variable
message = "I live in the Capital city of Punjab Province."
print(f'New message: {message}')

# 3. Personal Message
person_name = "Ishmal"
print(f"Hello {person_name}, would you like to learn some Python today!")

# 4. Name Cases
name = "Ishmal"
print(f"Lowercase: {name.lower()}")
print(f"Uppercase: {name.upper()}")
print(f"Titlecase: {name.title()}")



# 5. Famous Quote
print('Muhammad Ali Jinnah once said,"Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man..."')

# 6. Famous Quote 2
name = "Muhammad Ali Jinnah"
message = f'{name} once said,"Think a hundred times before you take a decision, but once that decision is taken, stand by it as one man..."'
print(message)

# 9. Variable Swap
a = "Lahore"
b = "Lhr"
print(f"Before Swapping a = {a} & b = {b}")
a, b = b, a
print(f"After Swapping a = {a} & b = {b}")

# 8. Variable Sum
x, y, z = 5, 10, 15
print(f"The sum is {x+y+z}")

# 10. Favorite Color
fav_color = "Royal Blue"
print(fav_color)
fav_color = "Electric Blue"
print(fav_color)

# 11. Changing Pet Name
pet_name = "Buddy"
pet_name = "Max"
print(pet_name)

# 12. Observing Name Error
try:
    sunshine = "SunShine"
    print(sunsine)  # This will cause a NameError
except NameError as e:
    print(f"Error: {e}")
# 13. Reassigning Score
score = 100
print(score)
score = 101
print(score)

# 14. City Name
city = "Lahore"
print(f"The favorite city is {city}.")

# 15. Title Case Text
text = "python programming"
print(text.title())

# 16. Lowercase Conversion
string = "LAhoRe."
print(string.lower())

# 17. Uppercase Conversion
string = "Lahore."
print(string.upper())

# 18. Current Temperature
temperature = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Printing a Poem
poem = "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate.\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date."
print(poem)

