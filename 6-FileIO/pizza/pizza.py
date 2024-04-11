import sys
import csv
from tabulate import tabulate


def main():
    # Check the number of command-line arguments
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        print("Error: File must be a .csv file")
        sys.exit(1)

    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        if not data:
            print("Error: The CSV file is empty")
            sys.exit(1)

        table = tabulate(data, headers="firstrow", tablefmt="grid")
        print(table)

    except FileNotFoundError:
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
