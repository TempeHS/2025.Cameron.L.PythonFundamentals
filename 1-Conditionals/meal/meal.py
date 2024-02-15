def convert(time):
    hours_str, _ = time.split(":")
    hour = int(hours_str)
    if 7 <= hour < 8:
        return "Breakfast"
    elif 12 <= hour < 13:
        return "Lunch"
    elif 18 <= hour < 19:
        return "Dinner"
    else:
        return "Nothing"


def main():
    time = input("What time is it (in HH:MM format)? ")
    mealtime = convert(time)
    print("Mealtime:", mealtime)


if __name__ == "__main__":
    main()
