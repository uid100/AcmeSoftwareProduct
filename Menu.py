#!/usr/bin/env python3

# Create a simple menu class

import Greeting


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
        print("\t\nOption 1 selected\n")

    def option2():
        print("\t\nOption 2 selected\n")

    menu = Menu({
        "hi": Greeting.say_hi,
        "bye": Greeting.say_bye,
        "hello": Greeting.say_hello,
        "goodbye": Greeting.say_goodbye,
        "1": option1,
        "2": option2,
        "quit": exit
    })
    menu.run()
