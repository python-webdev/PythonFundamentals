name = "John"
print(f"Hello {name}, would you like to learn some Python today?")

first_name = "Sarah"
print(first_name.lower())  # sarah
print(first_name.upper())  # SARAH
print(first_name.title())  # Sarah

quote = "Albert Einstein once said, 'A person who never made a mistake never tried anything new.'"
print(quote)

famous_person = "Albert Einstein"
message = f"{famous_person} once said, 'Imagination is more important than knowledge.'"
print(message)

full_address = " 123 Main Street\nAnytown, USA 12345 "
print(full_address.strip())  # "123 Main Street\nAnytown, USA 12345"

file_name = "example.txt"
print(file_name.removesuffix(".txt"))  # "example"


universe_age = 13_800_000_000
print(f"The universe is approximately {universe_age} years old.")

x, y, z = 0, 0, 0
print(f"x: {x}, y: {y}, z: {z}")

print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 // 2)

favorite_number = 63
print(f"My favorite number is {favorite_number}.")
