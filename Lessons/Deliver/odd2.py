integerList = [5,4,8,26,4,5]

 

def hacktober(integerList):
  oddCount = 0
  for i in range(len(integerList)):
    for j in range(len(integerList)):
      if i != j:
        
        result = integerList[i] + integerList[j]
        isOdd = result % 2 != 0

        if (isOdd) :
          oddCount = oddCount + 1

  return oddCount

#Test!
count = hacktober(integerList)
print(count, "odd numbers")


(( x + y) * z ) / 13

