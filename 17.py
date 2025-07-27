def greet(*, name, message="Hello"):
    print(f"{message}, {name}!")

# Call 1: providing both
greet(name="Pratyush", message="Good morning")

# Call 2: providing only name
greet(name="Pratyush")