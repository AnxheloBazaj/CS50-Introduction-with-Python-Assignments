def main():
    plate = input("Plate: ") # Promt the user for input (plate)
    if is_valid(plate): # check if the plate is valid via is_valid method and print valid if true
        print("Valid")
    else:               # print invalid if false
        print("Invalid")

def is_valid(s): # define is_valid function
    punctuation_marks = [' ',".", ",", "!", "?", ":", ";", "'",
                         '"', "(", ")", "[", "]", "{", "}", "<", ">"] # list with punctuation marks
    num =''  # placeholder variable which hold numeric characters from the license plate
    for i in s: #iterate over each character of the plate
        if i.isnumeric(): # check if a character is numeric and add it to num variable
            num+=i
        if i in punctuation_marks  : #check if a character is punctuation mark and if yes return false
            return False
    if s[0:2].isalpha(): #if the first two characters are letters countinue
        if  len(s)<2: # if the length of the plate is less than two return false
            return False
        elif len(s) <= 6 or len(s) == 2: #if the lengh is less than two or equal to two countinue
            if s.isalpha(): # if the plate is all alphabetic characters return true
                return True
            if  s.isalpha()==False:  # if the plate contains non alphabetic character continue
                if s[s.index(num[0]):].isnumeric(): #if the remaining part of the plate is all numbers continue
                    if len(num)!=0: # if the num variable has numeric characters continue
                        if num[0]=='0': # if the first character is '0' return false
                            return False
                        elif num[0]!='0': # if the first character is not '0' return true
                            return True
                elif s[s.index(num[0]):].isnumeric() == False: # #if the remaining part of the plate is not all numbers return false
                    return False
    else:
        return False

main()#call main
