def StringSort(stringList):
    print (sorted(stringList, key=len))
no = input("Number of strings to sort :")
stringList = []
for i in range(int(no)):
	stringList.append(input("Enter string"))	
StringSort(stringList)
