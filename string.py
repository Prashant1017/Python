def getMiddleThreeChars(sampleStr):
  middleIndex = int(len(sampleStr) /2)
  print(middleIndex)
  print("Original String is", sampleStr)
  middleThree = sampleStr[middleIndex-1:middleIndex+2]
  print("Middle three chars are", middleThree)
  
getMiddleThreeChars("abcdefgh")
getMiddleThreeChars("Jasonay")

import re

inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
  totalMarks+=mark

percentage = totalMarks/len(markList)  
print("Total Marks is:", totalMarks, "Percentage is ", percentage)
