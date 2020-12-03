inputd= open(r"C:\Users\John\Desktop\Work Python\AdventOfCode2020\AdventOfCode2020\2020day1\input.txt", "r")

data = []
value1 = 0
value2 = 0
value3 = 0
finalvalue= 0

#take input data from file and store in list
for i in inputd:
    value = int(i.strip())
    data.append(value)

inputd.close()

data.sort()
listlen = len(data)
#takes the starting number and look for two other numbers in the array that add up to 2020. if there are none, adjust the locations we should look in the array depending on if the total sum was too high or two low 
#This logic uses the two-pointer technique. More can be found on this online
# If you are having trouble understanding the two-pointer technique this video gives a good simple summary https://www.youtube.com/watch?v=dQw4w9WgXcQ
for i in range(0, listlen-2):
    l = i+1
    r = listlen-1
    while (l < r):
        if(data[i] + data[l] + data[r] == 2020):
            value1 = data[i]
            value2 = data[l]
            value3 = data[r]
            finalvalue = (value1*value2*value3)
            print(finalvalue)
            break
            #Because we sorted the data we know that if the value is lower we want to advance the lead of the l variable over the iteration value
        elif(data[i] + data[l] + data[r] < 2020):
                l += 1
        else:
                r -= 1