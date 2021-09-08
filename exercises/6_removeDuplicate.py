# write a function that takes in a list of integers 
# and returns true if it contains 008 in order
def removeDuplicate(word, n):
    s = set()

    for i in word:
        s.add(i)

    result = ""
    for i in s:
        result = result + i;
    return result

str = input("Insert the word with duplicate characters: ")
n = len(str)
print(removeDuplicate(list(str), n))