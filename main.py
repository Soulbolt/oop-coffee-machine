from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects and variables for the coffe machine functions
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_available = ""
is_machine_on = True

# Keep looping as long as machine is on is True
while is_machine_on:
    # Ask user to make a choice from given selection
    choice = input(f"What would you like? {menu.get_items()}\n")
    # Check if user's choice matches proper selection to make a coffee or produce reports or turn off machine
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_machine_on = False
        # Check if choice matches the menu item list
    elif choice in menu.get_items():
        coffee_available = menu.find_drink(choice)
        # Check if there are sufficient ingredients to make the coffee and return True
        if coffee_maker.is_resource_sufficient(coffee_available):
            # If sufficient ingredients request payment and check if coins inserted >= than the cost
            if money_machine.make_payment(coffee_available.cost):
                # If coins inserted cover cost, then make coffee
                coffee_maker.make_coffee(coffee_available)
            else:
                # If coins do not cover cost return message to user
                money_machine.make_payment(coffee_available.cost)
        else:
            # If not enough resource available, return message to user
            coffee_maker.is_resource_sufficient(coffee_available)
    else:
        # IF users choice does not match any of the expected options. return message
        menu.find_drink(choice)


