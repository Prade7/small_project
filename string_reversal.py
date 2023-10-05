
def string_reversal():
    input_string = input("Enter the string ")
    input_string = input_string.split()
    input_string = [x[::-1] for x in input_string]
    print(" ".join(input_string))
string_reversal()