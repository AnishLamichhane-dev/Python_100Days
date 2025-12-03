MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}
money = 0

def resources_sufficient(coffee_ingredients):
    """RETURNS True if the resources sufficient to make a coffee else RETURNS False."""
    enough_ingredient = True
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there isn't enough {ingredient}.")
            enough_ingredient = False
    return enough_ingredient

def coins():
    """Ask pennies, nickels, dimes, quarters from the user and RETURNS it."""
    print("Please insert coins.")
    coin = float(input("How many Pennies?: "))*0.01
    coin += float(input("How many Nickles?: "))*0.05
    coin += float(input("How many Dimes?: "))*0.10
    coin += float(input("How many Quarters?: "))*0.25
    return coin

def transaction(money_received, drink_cost):
    """RETURNS true if payment is sufficient else RETURNS False."""
    transaction_successful = True
    if money_received < drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
        transaction_successful = False
    else:
        global money
        change = round(payment - drink["cost"] , 2)
        print(f"Here is your {change}$ in change.")
        money += drink_cost
    return transaction_successful



def make_coffee(drink_name, coffee_ingredients):
    """Gives coffee to user and subtracts total resources from dictionary."""
    for each_item in coffee_ingredients:
        resources[each_item] -= coffee_ingredients[each_item]
    print(f"Here is your {drink_name}. Enjoy!")

machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/off):  ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = MENU[user_choice]
        if resources_sufficient(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
    else:
        print(f"Choose one of these options: espresso/latte/cappuccino/report/off")