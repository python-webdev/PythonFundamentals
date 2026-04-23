bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

print(bicycles[0].capitalize())
print(bicycles[2].upper())
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

names = ["Alice", "Bob", "Charlie", "Diana"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
message = f"Hello, {names[0]}!"
print(message)

message = f"Hello, {names[1]}!"
print(message)

message = f"Hello, {names[2]}!"
print(message)

message = f"Hello, {names[3]}!"
print(message)

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
print(f"The first motorcycle I owned was a {first_owned.title()}.")

too_expensive = "harley-davidson"
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.")
