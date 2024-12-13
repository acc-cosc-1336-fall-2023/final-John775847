import question_c

def main():
    while True:
        length = int(input("Enter the length of the multiplication table\n"))
        width = int(input("Enter the width of the multiplication table\n"))
        mult_list = question_c.create_mulitiplication_table(length, width)
        question_c.display_multiplication_table(mult_list)

        user_quit = input("Press 1 to quit\n")
        if user_quit == "1":
            break

if __name__ == '__main__':
    main()
