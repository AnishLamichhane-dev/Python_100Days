from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_item = MenuItem('name','water','milk','coffee','cost')

machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/off):  ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        machine_on = False
    elif user_choice == "espresso" or "latte" or "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost=drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print(f"Choose one of these options: espresso/latte/cappuccino/report/off")






