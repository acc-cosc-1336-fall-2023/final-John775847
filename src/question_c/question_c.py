
def create_mulitiplication_table(length, height):
    mult_list = [0]
    i1 = 1

    #Top line
    while i1 != length+1:
        mult_list.append(i1)
        i1 += 1
    mult_list.append("\n")

    i1 = 1

    while i1 != length+1:
        i2 = 1
        mult_list.append(i1) #Left line
        while i2 != height+1:
            mult_list.append(i1*i2) #Multiplication table
            i2 += 1
        mult_list.append("\n")
        i1 += 1

    return mult_list

def display_multiplication_table(mult_list):
    mult_string = ''
    for i in mult_list:
        mult_string += " " + str(i)
    print(mult_string)
