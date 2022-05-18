from drinks_database import drinks

starting_items = {
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money": 0,
    "continue": True,
}


def show_report():
    for items in starting_items["ingredients"]:
        print(items + ': ' + str(starting_items["ingredients"][items]), end="")
        if (items.lower().startswith("w")) or items.lower().startswith("mi"):
            print("ml")
        elif items.lower().startswith("coff"):
            print("g")
    print("money: $" + str(starting_items["money"]))


def check_ingredients():
    if coffee_choice.lower() == "espresso":
        for items in drinks[coffee_choice]["ingredients"]:
            if starting_items["ingredients"][items] < drinks[coffee_choice]["ingredients"][items]:
                print("Sorry, not enough " + items + ". Your money will now be refunded.")
                return False
            else:
                return True
    elif coffee_choice.lower() == "cappuccino":
        for items in drinks[coffee_choice]["ingredients"]:
            if starting_items["ingredients"][items] < drinks[coffee_choice]["ingredients"][items]:
                print("Sorry, not enough " + items + ". Your money will now be refunded.")
                return False
            else:
                return True
    elif coffee_choice.lower() == "latte":
        for items in drinks[coffee_choice]["ingredients"]:
            if starting_items["ingredients"][items] < drinks[coffee_choice]["ingredients"][items]:
                print("Sorry, not enough " + items + ". Your money will now be refunded.")
                return False
            else:
                return True
    elif coffee_choice.lower() == "report":
        show_report()
    else:
        print("Goodbye!")
        starting_items["continue"] = False


def check_coins():
    print('Please insert coins.')
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    total = int(quarters)*0.25 + int(dimes)*0.10 + int(nickles)*0.05 + int(pennies)*0.01
    if total >= drinks[coffee_choice]["price"]:
        for items in drinks[coffee_choice]["ingredients"]:
                starting_items["ingredients"][items] = starting_items["ingredients"][items] - drinks[coffee_choice]["ingredients"][items]
        starting_items["money"] = starting_items["money"] + drinks[coffee_choice]["price"]
        change = total - drinks[coffee_choice]["price"]
        print("Here is $" + str(round(change,2)) + " in change.")
        print("Here is your " + coffee_choice + ". Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")


while starting_items["continue"]:
    coffee_choice = input("Which coffee would you like? (espresso/cappuccino/latte)")
    if check_ingredients():
        check_coins()
