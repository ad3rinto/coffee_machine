from art import coffee_art

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
    "water": 600,
    "milk": 200,
    "coffee": 100,
}

status = True

def print_report(available_resource):
    """ prints a list of all available resources"""
    water_level = available_resource["water"]
    milk_level = available_resource["milk"]
    coffee_level = available_resource["coffee"]
    print(f" The machine has {water_level}ml, {milk_level}ml and {coffee_level}gm available")

def check_resources(option, available_resource):
    """ takes customer choice and validates there is enough ingredients to make their request"""
    if option == "latte" or option == "cappuccino":
        if (MENU[option]["ingredients"]["water"] > available_resource["water"] and
        (MENU[option]["ingredients"]["coffee"] ) > (available_resource["coffee"] and
        (MENU[option]["ingredients"]["milk"] ) > (available_resource["milk"]))):
            return False
        else:
            return True
    elif option == "espresso":
        if (MENU[option]["ingredients"]["water"] > available_resource["water"] and (MENU[option]["ingredients"]["coffee"]) > (available_resource["coffee"])):
            return False
        else:
            return True
    else:
        print("Invalid option")



def collect_payment(option, payment, available_resource):
    if payment >= MENU[option]["cost"]:
        change = payment - MENU[option]["cost"]
        # TODO: 8. If money is correct and resources enough, dispense drink
        print("......................Serving your drink")
        # TODO: 6. Deduct money and give change if applicable
        print(f"Here is your change of : £{change}")
    else:
        print("Insufficient funds, look for more money")



print (coffee_art)
while status:

    # TODO: 1. Prompt user to request their choice of drink

    customer_choice = input("What whould you like? (espresso/latte/cappuccino): \n").lower()
    # TODO: 2. Turn off the machine by entering "off".
    if customer_choice == "off":
        print("Turning ......off")
        status = False
    # TODO: 3. Print a report of all the coffee machine resources
    elif customer_choice == "report":
        print_report(resources)
    # TODO: 4. Check if available resources are enough for user's choice
    elif customer_choice == "latte" or customer_choice == "cappuccino" or customer_choice == "espresso":
        hello = check_resources(customer_choice, resources)
        if hello:
            # TODO: 5. Accept payment. Check if amount provided is enough for the drink requested
            paid_amount = float(input("How much do you have to spend ? : "))
            collect_payment(customer_choice, paid_amount, resources)
            # TODO: 7. deduct resources
            if customer_choice == "latte" or customer_choice == "cappuccino":
                resources["water"] = resources["water"] - MENU[customer_choice]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[customer_choice]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU[customer_choice]["ingredients"]["milk"]
            elif customer_choice == "espresso":
                resources["water"] = resources["water"] - MENU[customer_choice]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[customer_choice]["ingredients"]["coffee"]

        else:
            print("Insufficient funds, try again")
    else:
        print("You have entered an invalid option")























