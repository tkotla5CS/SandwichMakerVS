
# Tejas Kotla
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Insert coins please.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        return sum([quarters, dimes, nickels, pennies])

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")

# Initialize SandwichMachine with resources
machine = SandwichMachine(resources)

def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {machine.machine_resources['ham']} slice(s)")
            # Convert cheese from ounces to pounds for the report
            cheese_pounds = machine.machine_resources['cheese'] / 16
            print(f"Cheese: {cheese_pounds:.2f} pound(s)")
        elif choice in recipes:
            if machine.check_resources(recipes[choice]['ingredients']):
                coins = machine.process_coins()
                if machine.transaction_result(coins, recipes[choice]['cost']):
                    machine.make_sandwich(choice, recipes[choice]['ingredients'])
        else:
            print("Invalid choice. Please choose again.")

main()



