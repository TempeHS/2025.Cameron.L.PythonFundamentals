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
    "December",
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break
    except ValueError:
        try:
            month, day, year = date.split(" ")
            month = months.index(month) + 1
            day = day.rstrip(",")
            if 1 <= month <= 12 and 1 <= int(day) <= 31:
                break
        except ValueError:
            pass

print(f"{year}-{int(month):02d}-{int(day):02d}")
