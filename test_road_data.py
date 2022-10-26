from road_data import *
import pandas as pd
import pytest
import sys
import io

DATE = "date_time"
CARS = "no_of_cars"


@pytest.fixture
def roaddata():
    data = [["2021-12-02T00:00:00", 2],
            ["2021-12-04T01:30:00", 4],
            ["2021-12-05T02:00:00", 2],
            ["2021-12-05T01:30:00", 8]]
    df = pd.DataFrame(data)
    df.columns = (DATE, CARS)
    return df


def test_date_convert():
    date = convert_date("2021-12-02T00:00:00")
    assert str(date) == "2021-12-02"


def test_print_total_vehicles(roaddata):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_total_vehicles(roaddata)
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Total number of cars =  16\n"


def test_print_top_three_half_hours(roaddata):
    expected = '''Date and Time = 2021-12-05T01:30:00 Number of Cars =  8
Date and Time = 2021-12-04T01:30:00 Number of Cars =  4
Date and Time = 2021-12-02T00:00:00 Number of Cars =  2
'''
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_top_three_half_hours(roaddata)
    sys.stdout = sys.__stdout__
    print(capturedOutput.getvalue())
    assert capturedOutput.getvalue() == expected

def test_print_cars_per_day(roaddata):
    expected = '''Total vehicle in  2021-12-02 = 2
Total vehicle in  2021-12-04 = 4
Total vehicle in  2021-12-05 = 10
'''
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print_cars_per_day(roaddata)
    sys.stdout = sys.__stdout__
    print(capturedOutput.getvalue())
    assert capturedOutput.getvalue() == expected