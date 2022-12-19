# Python code to check if a
# given ISBN is valid or not.

# run this program and then just change json file in directory python file and save it
 
import json
import os
import time

def isValidISBN(isbn: str):
    print("Book number: ",isbn)
    print("lenght Book number: " ,len(isbn))
    # check for length
    if len(isbn) != 10:
        return False
     
    # Computing weighted sum
    # of first 9 digits
    _sum = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            _sum += int(isbn[i]) * (10 - i)
        else:
            return False
    print("calculated test number: ", _sum)
    # Checking last digit
    if(isbn[9] != 'X' and 0 <= int(isbn[9]) <= 9):
        return False
    
    # If last digit is 'X', add
    # 10 to sum, else add its value.
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])
     
    # Return true if weighted sum of
    # digits is divisible by 11
    print("remainder of the division: ",_sum % 11)
    print("ISBN-10 is correct" if _sum % 11==0 else "ISBN-10 is incorrect")
    return

# isbn = "007462542X"
# isbn="097522980X"

json.dump({"enter_your_isbn":None}, open('isbn.json', 'w')) # creat json file to enter yuor ISBN
f=0
while 1:
    time.sleep(0.05) # it for control use cpu
    try:
        if os.path.isfile("isbn.json"): # check if file exist in directory
            ISBN=json.load(open('isbn.json')) # take json file
            if ISBN["enter_your_isbn"]!=None: # check if you enter a new ISBN
                isbn=ISBN["enter_your_isbn"]
                isValidISBN(isbn)
                json.dump({"enter_your_isbn":None}, open('isbn.json', 'w'))
                f=0
        if f==0:
            print("enter your ISBN")
            f=1
    except Exception as error: #control error
        # print(error)
        pass
