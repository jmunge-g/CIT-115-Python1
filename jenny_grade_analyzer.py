# The program allows for the numeric entry of 4 test scores
# The code then compute the test average and determine a letter grade

# ask the user for name
name = input("Name of the person that we are calculating the grades for: ")

# take input of grades from the user
nTest1 = float(input("Test 1: "))
nTest2 = float(input("Test 2: "))
nTest3 = float(input("Test 3: "))
nTest4 = float(input("Test 4: "))

# we have to determine the lowest grade and decide to ignore or use it
# assuming that the lowest grade is the first test entered by the user
nLowestTest = nTest1

# search for the lowest test
if nTest2 < nLowestTest:
    # Note: we are comparing nTest1 (nLowestTest) with nTest2
    # if this is not true, nothing with be executed here
    # we will jump to the next if statement
    nLowestTest = nTest2
if nTest3 < nLowestTest:
    nLowestTest = nTest3
if nTest4 < nLowestTest:
    nLowestTest = nTest4
    
# on reaching here, we have the lowest grade
# the lowest grade is held by variable nLowestTest



nAverageScore = 0.0 # a variable to hold the average of scores

# ask the user if they wish to drop the lowest grade
res = input("Do you wish to Drop the Lowest Grade Y or N? ")
# we expect the user to enter y,Y, N or n
# capitalize is used to change the input to caps
if res.capitalize() == 'Y':
    # Drop the lowest test grade by subtracting from the rest
    nSumScores = (nTest1 + nTest2 + nTest3 + nTest4) - nLowestTest
    # calculate the average
    nAverageScore = nSumScores / 3

elif res.capitalize() == 'N':
    nSumScores = (nTest1 + nTest2 + nTest3 + nTest4)
    nAverageScore = nSumScores / 4
    # print(f"{name} test average is: {average_score}")
else:
    print("Enter Y or N to Drop the lowest Grade")
    # The program exits here
    exit(1)

# check for negative scores
if (nTest1 < 0 ) or (nTest2 < 0 ) or (nTest3 < 0 ) or (nTest4 < 0 ):
    print("Test scores must be greater than 0")
    # the program exit here if any score less than zero is found
    exit(1)
else:
    # if all test scores are positive (above zero)
    # all the code here is executed: display of scorer name, average score and the grade
    # average is formated to 1 decimal place as per the instructions
    print(f"{name} test average is: {nAverageScore:.1f}")

# we are here: we have the average of all grades
# we can determine the grade of the user
# remember that the following if elif statement is inside if else statement above
    if nAverageScore >= 97.0:
        print("Letter grade for the test is: A+") 
    elif 94.0 <= nAverageScore < 97.0:
        print("Letter grade for the test is: A") 
    elif 90.0 <= nAverageScore < 94.0:
        print("Letter grade for the test is: A-") 
    elif 87.0 <= nAverageScore < 90.0:
        print("Letter grade for the test is: B+") 
    elif 84.0 <= nAverageScore < 87.0:
        print("Letter grade for the test is: B")  
    elif 80.0 <= nAverageScore < 84.0:
        print("Letter grade for the test is: B-") 
    elif 77.0 <= nAverageScore < 80.0:
        print("Letter grade for the test is: C+") 
    elif 74.0 <= nAverageScore < 77.0:
        print("Letter grade for the test is: C")  
    elif 70.0 <= nAverageScore < 74.0:
        print("Letter grade for the test is: C-") 
    elif 67.0 <= nAverageScore < 70.0:
        print("Letter grade for the test is: D+") 
    elif 64.0 <= nAverageScore < 67.0:
        print("Letter grade for the test is: D")  
    elif 60.0 <= nAverageScore < 64.0:
        print("Letter grade for the test is: D-") 
    elif 0 <= nAverageScore < 60.0:
        print("Letter grade for the test is: F")  