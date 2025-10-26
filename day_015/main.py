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


def main():
    machine_is_on = True

    while machine_is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "off":
            machine_is_on = False



if __name__ == "__main__":
    main()


print_resources()
