# ------------------------------------------------------ #
# abstract : assignment 1 Question 3 Locker puzzle
# author : hhk
# time : 2022.10.13
# ------------------------------------------------------ #
print("Locker puzzle")
lockers=100
students=100

resultLockerIsOpen={}
print("\nLockers"),
for a in range(1,lockers+1):        # loop all lockers
    resultLockerIsOpen[a] = False
    for b in range (1,students+1):    # loop all students
        if a%b == 0:
            resultLockerIsOpen[a]= not resultLockerIsOpen[a]
    # print result
    if resultLockerIsOpen[a]:
        print("{},".format(a),end=" ")
print("\nare open")