import datetime
import sys
import inflect

p = inflect.engine()


class DOB:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


def get_DOB():
    DOBS = input("Enter date of birth \n" "In YYYY-MM-DD format: ")
    YYYY, MM, DD = DOBS.split("-")
    return DOB(int(YYYY), int(MM), int(DD))


def inmin(DOB):
    today = datetime.datetime.now()
    user_day = datetime.datetime(DOB.year, DOB.month, DOB.day)
    age_in_min = round((today - user_day).total_seconds() / 60)
    if age_in_min <= 0:
        return "Invalid date"
        sys.exit()
    return p.number_to_words(age_in_min)


def main():
    dob = get_DOB()
    test = inmin(dob)
    print("Age in minutes:", test)


if __name__ == "__main__":
    main()
