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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coffee_on = True
make_coffee = True


def check_resources(choice, water, milk, coffee):
    if water > resources['water']:
        return "Sorry, there is not enough water.", False
    elif coffee > resources['coffee']:
        return "Sorry, there is not enough coffee.", False
    elif milk > resources['milk'] and choice != "espresso":
        return "Sorry, there is not enough milk.", False
    else:
        return "", True


def dispense_drink(kcup):
    resources["water"] -= MENU[kcup]["ingredients"]["water"]
    resources["milk"] -= MENU[kcup]["ingredients"]["milk"]
    resources["coffee"] -= MENU[kcup]["ingredients"]["coffee"]


while coffee_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        coffee_on = False
        make_coffee = False
    elif order == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")
        make_coffee = False
    elif order == "latte":
        statement, move_on = check_resources(order, MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["milk"], MENU["latte"]["ingredients"]["coffee"])
        print(statement)
        make_coffee = move_on
    elif order == "espresso":
        statement, move_on = check_resources(order, MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"][0], MENU["espresso"]["ingredients"]["coffee"])
        print(statement)
        make_coffee = move_on
    elif order == "cappuccino":
        statement, move_on = check_resources(order, MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["milk"], MENU["cappuccino"]["ingredients"]["coffee"])
        print(statement)
        make_coffee = move_on

    while make_coffee:
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))

        total = (quarter * .25) + (dime * .10) + (nickle * .05) + (penny * .01)

        if total >= MENU[order]["cost"]:
            change = total - MENU[order]["cost"]
            resources["money"] += MENU[order]["cost"]
            print(f"Here is ${round(change,2)} in change.")
            print(f"Here is your {order} ☕️ Enjoy!")
            dispense_drink(order)
            make_coffee = False
        elif total < MENU[order]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            make_coffee = False

