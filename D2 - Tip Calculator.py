print("Welcome to the Tip Calculator")
total = float(input("What was the total of the Bill?\nIDR "))
interest = float(input("How much tip would you like to give? 10/11/15/20\n"))
people = int(input("How many people you want to split the bill wiht?\n"))

paid = round((total*((100+interest)/100)) / people, 2)

print(f"Each person should pay:\nIDR {paid}")
