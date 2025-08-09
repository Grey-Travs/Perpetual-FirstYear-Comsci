import pyfiglet

Kinemerut = pyfiglet.figlet_format("Hello, Perpetualites!")
Parting = pyfiglet.figlet_format("Thanks for Playing!")
border = "=" * (len(max(Kinemerut.splitlines(),key=len))+ 4)

print(border)
print(f"*{' ' * (len(border)-2)}*") 
for line in Kinemerut.splitlines():
    print(f"* {line.ljust(len(border)-4)} *")
print(f"*{' ' * (len(border)-2)}*")  
print(border)

print("Lets do some basic arithmetic operations:")
a = input("Enter First Number: ")
b = input("Enter Second Number: ")

x = float(a) + float (b)
print(f"The sum of {a} and {b} is: {x}")

print("Since I answered your question, Lets try to play a game!")
print("A guessing game!")

secret_number = 5
guess = int(input("Guess the secret number (between 1 and 10): "))

while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number!")
    elif guess > secret_number:
        print("Your guess is too high. Try again!")
    elif guess < secret_number:
        print("Your guess is too low. Try again!")

print(border)
print(f"*{' ' * (len(border)-2)}*") 
for line in Parting.splitlines():
    print(f"* {line.ljust(len(border)-4)} *")
print(f"*{' ' * (len(border)-2)}*")  
print(border)







