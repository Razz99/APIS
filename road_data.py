import pandas as pd
from dateutil import parser

# constants for dataframe column heading.
DATE = "date_time"
CARS = "no_of_cars"

# Gets date and time combined date and returns only date.
def convert_date(date_time):
    return parser.parse(date_time).date()

# Prints the total number of vehicles in the given input data in console.
def print_total_vehicles(df):
    print("Total number of cars = ", df[CARS].sum())

# Prints the top 3 half hours with heigh number of cars.
def print_top_three_half_hours(df):
    df.sort_values(by=[CARS], ascending=False, inplace=True)
    for item in pd.DataFrame(df.head(3)).index:
        print("Date and Time =", df[DATE][item],"Number of Cars = ", df[CARS][item])

# Prints the total number of cars per day.
def print_cars_per_day(df):
    df['formatted_date'] = df.apply(lambda row: convert_date(row.date_time), axis=1)
    unique_day = df.formatted_date.unique()
    for date in unique_day:
        print("Total vehicle in ", str(date), "=",
              df.loc[df['formatted_date'] == date, CARS].sum())


def main():
    try:
        df = pd.read_csv("input.txt", sep=" ", header=None)
    except:
        print("failed to read file")
    df.columns = (DATE, CARS)
    print("\n***** Displaying top three half hour cars in same date and time format as in input *****\n")
    print_top_three_half_hours(df)
    print("\n***** Displaying total number of cars *****\n")
    print_total_vehicles(df)
    print("\n***** Displaying total number of cars per day *****\n")
    print_cars_per_day(df)

if __name__ == "__main__":
    main()
