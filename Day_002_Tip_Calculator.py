print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ \n"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? \n"))
people = float(input("How many people to split the bill? \n"))
tip_bill = bill + bill*(tip/100)
final_bill = tip_bill / people
end_bill = round(final_bill, 2)
print(f"Each person should pay: ${end_bill}")
