import random
import string

# Functions

# GetLote() is a function that generates the Lote serial number by parts, as shown below:

def getLote():

    # First, we create a dynamic array to start pumping characters and numbers.

    SerialLote = [] 

    # The fist character in every Pringles can is always a letter "L", so its the first letter
    # that is inserted
    
    SerialLote.append("L")

    # The next four characters are numbers that are randomly generated using the ranint(a,b) 
    # function, then toose numbers are converted to strings and placed in our initialy created
    # array. 
    
    for i in range(4):

        n = random.randint(0,9)
        SerialLote.append(str(n))

    # The next two caracters are uppercase lettes, also randomly generated. Don’t ask me about. 
    # the function that generates that because I stole that solution from StackOverflow.
    
    for i in range(2):

        character = string.ascii_uppercase
        SerialLote.append( ''.join(random.choice(character) for i in range(1)))

    # The next 6 characters are numbers, and as you thought, they are also randomly generated.    

    for i in range(6):

        n = random.randint(0,9)
        SerialLote.append(str(n))

    # This portion of the code converts the previusly filled array into a string using the
    # join() function. 

    separator = ""

    finalCode = separator.join(SerialLote)

    # Finally, it returns the string containing the Lote code.

    return finalCode

# Similar to the previous function, this getExpirationDate() generates a randomly selected 
# date between 2022 and 2023. 

def getExpirationDate():

    # We create the array that will store the date.

    expirationDate = []

    # Then we choose the expiration month, of course bewteen 01 and 12 because Undecimber does not exist.

    monthDate = random.randint(1,12)

    # This is important because if the month has only one digit. Then this code below places a 0 into the 
    # array to fullfill that space. Otherwise, the web will not accept the entered number. 

    if (monthDate <= 9):

        expirationDate.append("0")

    expirationDate.append(str(monthDate))

    # Then we randomly generate the year. As I said, bewteen 2022 and 2023, you can change this is you want. 

    yearDate = random.randint(2022, 2023)

    expirationDate.append(str(yearDate))
    
    # And finally, this convert the array into a string to return it propely. 

    separator = ""

    finalDate = separator.join(expirationDate)

    return finalDate

# Just making sure the code works at this point.

print(getLote())

print(getExpirationDate())




    

