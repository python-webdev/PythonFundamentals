# ============================================================
# LISTS IN PYTHON
# ============================================================
# A list is a mutable, ordered sequence of items.
# Items can be of any type and duplicates are allowed.
# Syntax: my_list = [item1, item2, item3]

# --- Accessing Items by Index ---
# Indices start at 0. Negative indices count from the end (-1 is last).
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(f"{bicycles}\n")

print(bicycles[0].capitalize())  # index 0  → first item
print(bicycles[2].upper())  # index 2  → third item
print(bicycles[-1])  # index -1 → last item
message = f"My first bicycle was a {bicycles[0].title()}."
print(f"{message}\n")

# --- Using Index Values in Messages ---
# f-strings let you embed list items directly in a string.
names = ["Alice", "Bob", "Charlie", "Diana"]
print(names[0])
print(names[1])
print(names[2])
print(f"{names[3]}\n")

# --- Building Personalised Messages ---
message = f"Hello, {names[0]}!"
print(message)

message = f"Hello, {names[1]}!"
print(message)

message = f"Hello, {names[2]}!"
print(message)

message = f"Hello, {names[3]}!"
print(f"{message}\n")

# --- Negative Indexing in an f-string ---
motorcycles = ["honda", "yamaha", "harley-davidson"]
print(motorcycles)
message = f"I would like to own a {motorcycles[-1].title()} motorcycle."
print(f"{message}\n")

# Modifying, Adding, and Removing Elements
motorcycles[0] = "jawa"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

motorcycles.insert(1, "ducati")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")
motorcycles = ["honda", "yamaha", "suzuki", "harley-davidson"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")

too_expensive = "harley-davidson"
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.\n")

guests = ["Alice", "Bob", "Charlie", "Diana"]
invite_message = "You are invited to dinner, "
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.\n")

guests[1] = "John"
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.\n")

guests.insert(0, "Emily")
guests.insert(2, "Michael")
guests.append("Sarah")
print(f"Guests: {guests}\n")
print(f"{invite_message}{guests[0]}.")
print(f"{invite_message}{guests[1]}.")
print(f"{invite_message}{guests[2]}.")
print(f"{invite_message}{guests[3]}.")
print(f"{invite_message}{guests[4]}.")
print(f"{invite_message}{guests[5]}.")
print(f"{invite_message}{guests[6]}.\n")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
print(f"{guests}\n")

del guests[1]
del guests[0]
print(f"Guests list: {guests}\n")

# Organising a List
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original cars list: {cars}")
# Sorting a List Permanently with the sort() Method
cars.sort()
print(f"Sorted cars: {cars}")
cars.sort(reverse=True)
print(f"Reverse sorted cars: {cars}\n")

# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original cars list: {cars}")
print(
    f"Temporarily sorted cars: {sorted(cars)}"
)  # sorted(reversed=True) can also be used to sort in reverse order
print(f"Original cars list after sorted(): {cars}")
# Printing a List in Reverse Order
cars.reverse()
print(f"Cars in reverse order after reverse(): {cars}\n")

# Finding the Length of a List
cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Number of cars: {len(cars)}\n")

places = ["paris", "new york", "tokyo", "sydney", "rome"]
print(f"Original places list: {places}")
print(f"Temporarily sorted places: {sorted(places)}")
print(f"Original places list after sorted(): {places}")
print(f"Temporarily reverse sorted places: {sorted(places, reverse=True)}")
print(f"Original places list after reverse sorted(): {places}")
places.reverse()
print(f"Places in reverse order after reverse(): {places}")
places.sort()
print(f"Places sorted permanently: {places}")
places.sort(reverse=True)
print(f"Places reverse sorted permanently: {places}\n")

print(f"Number of guests: {len(guests)}\n")

mountains = ["everest", "k2", "kangchenjunga", "lhotse", "makalu"]

print(f"Original mountains list: {mountains}")
mountains.append("cho oyu")
print(f"Mountains after append(): {mountains}")
mountains.insert(2, "manaslu")
print(f"Mountains after insert(): {mountains}")
del mountains[1]
print(f"Mountains after del: {mountains}")
popped_mountain = mountains.pop()
print(f"Mountains after pop(): {mountains}")
print(f"Popped mountain: {popped_mountain}")
mountains.remove("manaslu")
print(f"Mountains after remove(): {mountains}")
mountains.sort()
print(f"Mountains after sort(): {mountains}")
mountains.sort(reverse=True)
print(f"Mountains after reverse sort(): {mountains}")
mountains.reverse()
print(f"Mountains after reverse(): {mountains}")
print(f"Number of mountains: {len(mountains)}\n")

# Avoiding Index Errors When Working with Lists
motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles[3]) This will raise an IndexError because there is no index 3 in the motorcycles list

print(
    motorcycles[-1]
)  # This will print the last item in the list, which is "suzuki"
motorcycles = []

# print(motorcycles[-1]) This will raise an IndexError because the motorcycles list is empty

# Looping Through an Entire List
magicians = ["alice", "bob", "charlie"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# Doing something after a for loop
print("Thank you, everyone. That was a great magic show!\n")

pizzas = ["pepperoni", "mushroom", "extra cheese"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    print(f"{pizza.title()} pizza is my favorite!\n")
print("I really love pizza!\n")

animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# Using the range() Function
for value in range(1, 5):
    print(value, end=" ")
print()

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = []
for value in range(1, 11):
    squares.append(
        value**2
    )  # Exponentiation operator (**) is used to calculate the square of the value
print(f"Squares from 1 to 10: {squares}\n")

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Digits: {digits}")
print(f"Minimum digit: {min(digits)}")
print(f"Maximum digit: {max(digits)}")
print(f"Sum of digits: {sum(digits)}\n")

# List Comprehensions
# Syntax: [expression for item in iterable if condition]
squares = [value**2 for value in range(1, 11)]
print(f"Squares from 1 to 10 using list comprehension: {squares}")
even_squares = [value**2 for value in range(1, 11) if value % 2 == 0]
print(f"Even squares from 1 to 10 using list comprehension: {even_squares}\n")

list_of_one_to_twenty = list(range(1, 21))
print("Numbers from 1 to 20:")
for number in list_of_one_to_twenty:
    print(f"{number} ", end="")
print("\n")

list_of_one_to_twenty = [number for number in range(1, 21)]
print("Numbers from 1 to 20 using list comprehension:")
print(f"{list_of_one_to_twenty}\n")

numbers = list(range(1, 1_000_001))
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}\n")

odds = list(range(1, 21, 2))
print("Odd numbers from 1 to 20:")
for number in odds:
    print(f"{number} ", end="")
print("\n")

odds = [number for number in range(1, 21) if number % 2 != 0]
print("Odd numbers from 1 to 20 using list comprehension:")
print(f"{odds}\n")

# Threes: multiples of 3 from 3 to 30
threes = list(range(3, 31, 3))
print("Threes from 3 to 30:")
for number in threes:
    print(number, end=" ")
print("\n")

trees = [number for number in range(3, 31) if number % 3 == 0]
print("Threes from 3 to 30 using list comprehension:")
print(f"{trees}\n")

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(f"Cubes from 1 to 10: {cubes}\n")

# Using a List Comprehension to Generate a List of Cubes
cubes = [value**3 for value in range(1, 11)]
print(f"Cubes from 1 to 10: {cubes}\n")

# Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(f"Players: {players}")
print(f"First three players: {players[:3]}")
print(f"Players from index 1 to 3: {players[1:4]}")
print(f"Players from index 2 to the end: {players[2:]}")
print(f"Last three players: {players[-3:]}\n")

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("\n")

# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My favorite foods: {my_foods}")
print(f"My friend's favorite foods: {friend_foods}\n")

buses = ["volvo", "mercedes", "scania", "man", "iveco"]
print(buses[:3])  # Slicing the first three items
print(buses[1:4])  # Slicing from index 1 to 3
print(f"{buses[-3:]}\n")  # Slicing the last three items

my_pizzas = ["pepperoni", "mushroom", "extra cheese"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("hawaiian")
friend_pizzas.append("veggie")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")
print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
print("\n")

print("My foods are:")
for food in my_foods:
    print(f"- {food}")
print("\n")

print("My friend's foods are:")
for food in friend_foods:
    print(f"- {food}")
print("\n")

characters = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 28, "city": "Miami"},
    {"name": "Ethan", "age": 32, "city": "Seattle"},
]
