inputd= open(r"C:\Users\John\Desktop\Work Python\AdventOfCode2020\AdventOfCode2020\2020day1\input.txt", "r")

data = []
searchvalue = 0
value1 = 0
value2 = 0
finalvalue= 0
#take input data from file and store in list
for i in inputd:
    value = int(i.strip())
    data.append(value)

inputd.close()
#print(data)

#looks at each value and finds the value needed. Looks in the list for said value if it is found exit the loop
for i in data:
    searchvalue = 2020-i
    if searchvalue in data:
        value1 = i
        value2 = searchvalue
        break

#print (value1, value2)

final = value1*value2
print(final)