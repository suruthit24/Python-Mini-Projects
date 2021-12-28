weight = int(input("What is your weight? "))
unit = input("Enter 'lbs' for pounds or 'kilos' for kilos ")
if unit == "lbs":
    converted_weight = weight / 0.45
    print(f"You weigh {converted_weight} pounds")
elif unit == "kilos":
    converted_weight = weight * 0.45
    print(f"You weigh {converted_weight} kilos")
else:
    print("Invalid input")