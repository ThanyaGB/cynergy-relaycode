

def roman_num_to_int(string):
    roman_int = {"I":1,"X":10,"V":5,"L":50,"C":100,"D":500,"M":1000}
    int_val = 0
    length = len(string)
 
    
    for i in range(length,0):
        if string[i] == "M":
            int_val += roman_int["M"]
            continue
        elif string[i] == "D":
            if string[i-1] == "C":
                int_val += (roman_int["D"] - roman_int["C"])
            elif string[i+1] == "L":
                int_val += (roman_int["D"] + roman_int["C"])
            else:
                int_val += roman_int["D"]
        elif string[i] == "C":
            if string[i-1] == "L":
                int_val += (roman_int["C"] - roman_int["L"])
            else:
                int_val += roman_int["C"]
        elif string[i] == "L":
            if string[i-1] == "X":
                int_val += (roman_int["L"] - roman_int["X"])
            else:
                int_val += roman_int["L"]
        elif string[i] == "X":
            if string[i-1] == "V":
                int_val += (roman_int["X"] - roman_int["V"])
            else:
                int_val += roman_int["X"]
        elif string[i] == "V":
            if string[i-1] == "I":
                int_val += (roman_int["V"] - roman_int["I"])
            else:
                int_val += roman_int["V"]
        elif string[i] == "I":
                int_val += roman_int["I"]
                continue









x= input("Enter a roman numbers: ")
y= input("Enter another roman numbers: ")

sum = roman_num_to_int(x) + roman_num_to_int(y)
print(roman_num_to_int(sum))


#Thanya G B 
