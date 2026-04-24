bicycles = ["trek", "cannondale", "redline", "specialized"]
print(f"{bicycles}\n")

print(bicycles[0].capitalize())
print(bicycles[2].upper())
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(f"{message}\n")

names = ["Alice", "Bob", "Charlie", "Diana"]
print(names[0])
print(names[1])
print(names[2])
print(f"{names[3]}\n")

message = f"Hello, {names[0]}!"
print(message)

message = f"Hello, {names[1]}!"
print(message)

message = f"Hello, {names[2]}!"
print(message)

message = f"Hello, {names[3]}!"
print(f"{message}\n")

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
    print(value)
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
