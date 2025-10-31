year = int(input("Enter the year \n >>>"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR!!!")
        else:
            print("not!!! LEAP YEAR")
    else:
        print("LEAP YEAR!!!")
else:
    print("not!!! LEAP YEAR")
