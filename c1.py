a = input()
numberlist = str(input()).split()
start_to_end = str(input()).split()

goal = 0
i = int(start_to_end[0])

if int(start_to_end[0]) == int(start_to_end[1]):
    goal = int(numberlist[int(start_to_end[0])-1])
else:
    while i <= int(start_to_end[1]):
        goal = goal + int(numberlist[i-1])
        i += 1

count = 0

for i, val in enumerate(numberlist, start=1):

    test = i
    initial = True
    tempres = int(val)
    while True:
        if initial == True:
            if tempres == goal:
                count += 1
                break
            initial = False
        else:
            try:
                tempres = tempres + int(numberlist[test])
                if tempres > goal:
                    break
                elif tempres == goal:
                    count += 1
                    break
                else:
                    test += 1
            except:
                break

print(count)