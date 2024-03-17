import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    time = input("Date: ")
    try:
        m, d, y = time.split('/')
        y = y.strip()

        if int(m) >= 1 and int(m) <= 12 and int(d) >= 1 and int(d) <= 31:
          break
    except:
        try:
            if ',' not in time:
                raise ValueError

            m, d, y = time.split(' ')
            y = y.strip()
            d = d.strip()
            m = m.strip()

            for i in range(len(months)):
                if m == months[i]:
                    m = i + 1

            d = d.replace(',','')
            if int(m) >= 1 and int(m) <= 12 and int(d) >= 1 and int(d) <= 31:
                break
        except:
            pass


print(f'{y}-{int(m):02}-{int(d):02}')
