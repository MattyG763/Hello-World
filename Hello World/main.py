# System outputs hello world to the console


# Ask the user their name
def name():
    return input("What is your name? ")

# Print name to the console
def print_name(name):
    print(f"Hello, {name}")

def main():
    print_name(name())

main()