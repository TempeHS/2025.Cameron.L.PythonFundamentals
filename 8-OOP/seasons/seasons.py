from datetime import date
import sys


class DOB:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


def get_DOB():
    input("Enter date of birth \n" "In YYYY-MM-DD format")


def inmin():
    today = date.today()
    user_day = datetime.date(get_DOB())
    DOB_today = date._sub_(today, user_day)
    if DOB_today <= 0:
        return "Invalid date"
        raise ValueError
        sys.exit
    timedelta(DOB_today)


def timedelta():
    timedelta(
        days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
    )


def main():

    DOB = get_DOB
    print(DOB)
    DOBS = inmin()
    print(DOBS)


if __name__ == "__main__":
    main()
