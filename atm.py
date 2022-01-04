import random


class ATM():
    def __init__(self):
        print("Hello! Welcome to the ATM!")
        self.cardNO = int(input("Please enter your card number: "))
        self.pinNO = int(input("Please enter your pin number: "))

    def Ask(self):

        def menu():
            print("\nWhat do you want to do?")
            print("[1] Withdraw Cash")
            print("[2] Check Balance")
            print("[3] Take Loan")
            print("[0] Exit the progam")

        menu()
        option = input("\nEnter your option : ")

        while option != "0":
            if option == "1":
                print("\nCash has been withdrawn")
            elif option == "2":
                balance = random.randrange(100000, 900000)
                print(f"\nYour balance is ₹{balance}")
            elif option == "3":
                print("\nYour loan has been issued")
            else:
                print("\n!! Invalid Option !!")

            menu()
            option = input("\nEnter your option : ")

        print("\nThank you for using our services. ")


User = ATM()
User.Ask()