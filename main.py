
def main() -> None:
    print("Welcome to the AustinProgramRunner, how may I help you?")
    number_options = [1, 2, 3]  # will help with input edge cases
    if has_binding():
        number_options.append(4)

    while True: #part of input error handling, see further in function
        if has_binding():
            print("1) Make new binding")
            print("2) Edit existing binding")
            print("3) About") #explain purpose of program and such
            print("4) Exit") #exits the program
        else:
            print("1) Make new binding")
            print("2) About") #explain purpose of program and such
            print("3) Exit") #exits the program

        try: #in case value exception
            number = int(input("Please type the associated integer from one of the options above: "))
        except Exception as e: #handling incorrect value
            print("\n" + "Error: not an integer. No words or other types allowed!")
            print("Example input: 1")
            print(f"{"-" * 20}")
            continue
        if number not in number_options:
            print("\n" + "Please enter a valid integer option")
            print(f"{"-" * 20}")
        else:
            break


def has_binding() -> bool:
    return True

if __name__ == '__main__':
    main()