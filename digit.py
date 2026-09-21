#take input from user and find out how much input is digits
n = int(input("Enter a number: "))
num = sum(1 for c in str(n))
print(f"Number of digits in the input: {num}")