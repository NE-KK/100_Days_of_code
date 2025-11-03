# 100 Days of code by Angela Yu
# Day 15 - Coffee machine


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
}

bank = {
    "money": 0,
}


def print_resources():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")

    print(f"{bank} : ${bank['money']}")


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in [0.25, 0.10, 0.05, 1.00]:
        num_coins = int(input(f"How many {coin} coins?: "))
        total += num_coins * coin
    return total


def main():
    print(MENU)
    print('latte' in MENU)
    machine_is_on = True

    while machine_is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "off":
            machine_is_on = False

        if user_input == "report":
            print_resources()

        if user_input in MENU:
            resources_sufficient = check_resources(MENU[user_input]["ingredients"])
            money_received = 0
            
            if resources_sufficient:
                print("Please insert coins.")
                money_received = process_coins()
            else:
                print("Sorry, there is not enough resources.")

            if money_received >= MENU[user_input]["cost"]:
                change = round(money_received - MENU[user_input]["cost"], 2)
                print(f"Here is ${change} in change.")
                bank["money"] += MENU[user_input]["cost"]

                for item in MENU[user_input]["ingredients"]:
                    resources[item] -= MENU[user_input]["ingredients"][item]

                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")


if __name__ == "__main__":
    main()
