bloodtype = input().split(" ")

mom = bloodtype[0]
dad = bloodtype[1]

momlist = []
dadlist = []
completelist = []

for i in mom:
    momlist.append(i)

for i in dad:
    dadlist.append(i)


def find_blood(a, b):
    if a == "A" and b == "A":
        return "A"
    elif a == "A" and b == "O":
        return "A"
    elif a == "O" and b == "A":
        return "A"
    elif a=="A" and b=="B":
        return "AB"
    elif a == "B" and b == "A":
        return "AB"
    elif a == "B" and b == "B":
        return "B"
    elif a == "B" and b == "O":
        return "B"
    elif a == "O" and b == "B":
        return "B"
    elif a == "O" and b == "O":
        return "O"

def in_order(completelist):
    order = ["A", "AB", "B", "O"]

    newlist = []

    for i in order:
        if i in completelist and i not in newlist:
            newlist.append(i)
    return newlist

for i in mom:
    momlist.append(i)
for i in dad:
    dadlist.append(i)

for i in momlist:
    for v in dadlist:
        completelist.append(find_blood(i, v))

reallist = in_order(completelist)

res = ""
real = False
for i in reallist:
    if real == False:
        res = res + i
        real = True
    else:
        res = res + " " + i

print(res)