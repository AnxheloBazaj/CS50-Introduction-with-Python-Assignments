def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuation_marks = [' ',".", ",", "!", "?", ":", ";", "'", '"', "(", ")", "[", "]", "{", "}", "<", ">"]
    num =''
    stri=s
    #for i in s:

    for j in s:
        if j.isnumeric():
            num+=i
        elif j in punctuation_marks or len(s)<2 :
            return False
        if s[0:2].isalpha() and s.startswith('O') == False :
            if len(s) <= 6 or len(s) >= 2:
                if s.isalpha():
                    return True
                elif  s.isalpha()==False:
                    if s[s.index(num[0]):].isnumeric():
                        if len(num)!=0:
                          if num[0]=='0':
                            return False
                          elif num[0]!='0':
                            return True
                    elif s[s.index(num[0]):].isnumeric() == False:
                        return False
main()
