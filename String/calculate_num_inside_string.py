#sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5

def sumAndAverage(marks):

    # convert the type from the string to List
    convertToList = marks.split()
    # calcualting the half of indext length
    indexLen = int(len(convertToList)/2)
    # defining empty list to put the digits in side it
    digitList = []
    # intialzing sum
    sum = 0

    # 1st for loop: looping through the "convetToList" to figure out numbers
    for i in convertToList:
        if i == "78":
            digitList.append(convertToList[indexLen-4])
        elif i == "83":
            digitList.append(convertToList[indexLen-1])
        elif i == "68":
            digitList.append(convertToList[indexLen+2])
        elif i == "65":
            digitList.append(convertToList[indexLen+5])

    # 2nd for loop: iterating in each element to chage it to int
    for i in range(0, len(digitList)):
        digitList[i] = int(digitList[i])

    # 3nd for loop: calcaulating sum,avarage and print them
    for i in digitList:
        sum = sum + i
    print(sum)
    print(sum/int(len(digitList)))


# calling the function
sumAndAverage("English = 78 Science = 83 Math = 68 History = 65")
