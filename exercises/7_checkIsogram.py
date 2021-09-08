# check if string is isogram (word in which no letter occurs more than once)
def is_isogram(word):
    theWord = sorted(word)
    
    for x in range(len(theWord)):
        if theWord[x] == theWord[x+1]:
            return False         
    return True 

myString = input("Enter the word: ")
print(is_isogram(myString))