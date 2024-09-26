#!/usr/bin/env python3

# Create a simple menu class

class Menu:
    def __init__(self, options):
        self.options = options

    def display_menu(self):
        print("Menu:")
        for key, value in self.options.items():
            print(f"{key}. {value}")

    def get_choice(self):
        while True:
            choice = input("Enter your choice: ")
            if choice in self.options:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_choice()
            if choice == "quit":
                break
            else:
                self.options[choice]()


if __name__ == "__main__":
    def option1():
        print("Option 1 selected")

    def option2():
        print("Option 2 selected")

    menu = Menu({
        "1": option1,
        "2": option2,
        "quit": exit
    })
    menu.run()
