studentcount = int(input())

day = 1
date = 1
month = 3

totalcount = 1

daybefore = 1

monthdict = {
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 30,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

def find_if_so(day):
    day = int(day)
    i = 1

    hit = 0
    
    if day == 1:
        return False
    else:
        while i*i<=day:
            if day%i == 0:
                hit += 1
                if hit >= 2:
                    return False
            i += 1
        return True


while True:
    if totalcount >= studentcount:
        break

    totalday = monthdict[str(month)]
    if date > totalday:
        date = 1
        month += 1

    if find_if_so(date) == True:
        totalcount = totalcount + daybefore*3
        daybefore = daybefore*3
        day += 1
        date += 1
    else:
        totalcount = totalcount + daybefore*2
        daybefore = daybefore*2
        day += 1
        date += 1
    
    print(f"Day {day}\n{month}월 {date}일\n총 {totalcount}명, 이전 날 {daybefore}명\n")

print(day)