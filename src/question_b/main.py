import question_b

def dna_string1_maker():
    dna_string1 = ""
    while True:
        dna_string1 = input("Provide a DNA string greater than 8 characters but less than or equal to 16\n")
        if len(dna_string1) > 8 and len(dna_string1) <= 16:
            break
    return dna_string1

def dna_string2_maker():
    dna_string2 = ""
    while True:
        dna_string2 = input("Provide a DNA substring of exactly 4 characters\n")
        if len(dna_string2) == 4:
            break
    return dna_string2

def main():
    while True:
        dna_string1 = dna_string1_maker()
        dna_string2 = dna_string2_maker()
        print("\nYour result ", question_b.get_most_likely_ancestor_consensus(dna_string1, dna_string2))

        user_continue = input("Type 1 to continue\n")
        if user_continue != "1":
            break

if __name__ == '__main__':
    main()
