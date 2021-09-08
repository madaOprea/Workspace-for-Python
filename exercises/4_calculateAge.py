from datetime import datetime

def main():
    date = datetime.now()
    year = int(date.year)
    month = int(date.month)
    day = int(date.day)
    input_year = int(input("Enter the year you were born: "))
    if input_year <= 0 or input_year > 2020:
        print(" Don't you know your birthday??")
        exit()
    input_month = int(input("Enter the month you were born: "))
    if input_month <= 0 or input_month > 12:
        print(" Don't you know your birthday??")
        exit()
    input_day = int(input("Enter the day you were born: "))
    if input_day <= 0 or input_day > 31:
        print(" Don't you know your birthday??")
        exit()
    age_year = year - input_year
    age_month = month - input_month
    if age_month < 0:
        age_year = age_year - 1
        age_month = 12 - (input_month - month)
    age_day = day - input_day
    if age_day < 0:
        age_month = age_month - 1
        age_day = 31 - (input_day - day)
    print("you are " + str(age_year) + " years, " + str(age_month) + " months and " + str(age_day) + " days old.") 

if __name__ == "__main__":
    main() 