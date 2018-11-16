# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# Exercise 7-6
# prompt = 'Please tell me how old you are:'
# active = True
# while active:
#     year = input(prompt)
#     if year == 'quit' or year == 'exit':
#         active = False
#         continue
#     else:
#         year = int(year)
#     if year <= 3:
#         print('you got a free ticket.')
#     elif year <= 12:
#         print('The price is 10 bucks.')
#     elif year > 12:
#         print('The price is 15 bucks.')

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

