'''
Requirement:
There are three types of car to be parked in parking
1.Rickshaw ---> Amount = 100
2.Normal Car --- > Amount = 200
3.Buses --- > Amount = 300
'''
amount = 0
numbers_of_car = 0
maximum = 5
print("press 1 for Rickshaw")
print("press 2 for Normal Car")
print("Press 3 for Bus")
print("press 4 for showing Record")
print("press 5 for Delete the records")
print("press 6 to exit()")
while True:
    user_input = int(input("Enter a Number:"))
    if user_input == 1:
        if maximum > numbers_of_car:
            amount += 100
            numbers_of_car += 1
        else:
            print("Parking full")
    elif user_input == 2:
        if maximum > numbers_of_car:
            amount += 200
            numbers_of_car += 1
        else:
            print("Parking full")
    elif user_input == 3:
        if maximum > numbers_of_car:
            amount += 300
            numbers_of_car += 1
        else:
            print("Parking full")
    elif user_input == 4:
        print(f"Total Amount is {amount} Parked Cars {numbers_of_car}")
    elif user_input == 5:
        amount = 0
        numbers_of_car = 0
    elif user_input == 6:
        break
    else:
        print("Key does not exiest")
