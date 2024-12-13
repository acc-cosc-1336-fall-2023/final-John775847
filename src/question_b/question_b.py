
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    result = []

    for i in range(len(dna_string1)):
        if dna_string1[i:i+len(dna_string2)] == dna_string2:
            result.append(i+1)

    result = tuple(result) #Because of the instructions "as multiple Python parameters (not a string or list)", "returns the multiple parameters 2 4 10 (save each value to a variable)", and "Return: All locations of t as a substring of s.", I decided to use a tuple because it is aparently what python uses when you use a return statement with multiple variables.

    return result #Running the function with the return statement changed to "return 2, 4, 10" will still lead to a passing result for the assertEqual test made for this question. I believe thatis enough tp prove my assumption about tuples.
