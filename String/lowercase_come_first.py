""" arrange String characters such that lowercase letters should come first
Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first.

Expected Output:

input_String = PyNaTive
arranging characters giving precedence to lowercase letters
aeiNPTvy

arranging characters giving precedence to lowercase letters:
yaivePNT """



# input difination
input_String = "PyNaTive"

# list Declaration
List = []
lowerList = []
upperList = []
# looping counter
counter = 0

# looping to convert string to List
for i in input_String:
    List.append(i)

# condation
while(counter <= int(len(List)/2)):

    # for loop to itrate for each element in the List
    for i in List:

        # defining boolean
        isLower = i.islower()
        isupper = i.isupper()
        # if isLower append it to lowerList
        if isLower:
            lowerList.append(i)

        # if isUpper append it to upperList
        elif isupper:
            upperList.append(i)

        # every itration increase the counter by 1
        counter += 1

# adding upperList to lowerList
lowerList.extend(upperList)

# converting the list to string
sortedString = ''.join(lowerList)

# print the output
print(sortedString)
