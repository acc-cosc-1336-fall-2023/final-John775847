import question_a

def main():
    while True:
        user_input = int(input("[1] Display stock purchase history\n[2] Exit\n"))
        if user_input == 1:
            print()
            question_a.stock_purchase_history()
        elif user_input == 2:
            print()
            break
        else:
            print("\nYou must enter [1 or 2]")

if __name__ == '__main__':
    main()
