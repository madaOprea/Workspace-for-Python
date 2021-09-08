# write a function that takes in a list of integers 
# and returns true if it contains 008 in order
def spy_game(nums):
    spy = False

    for i in range(0, len(nums)-2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 8:
            spy = True

    return spy; 

def main():
    no = int(input("Enter the length of array: "))
    if no <= 0:
        print('This is not a positive number! ')
        no = int(input("Please enter the length of array: "))
    a = []
    for i in range(0, no):
        elem = int(input())
        a.append(elem)


    print(spy_game(a))

if __name__ == "__main__":
    main()

