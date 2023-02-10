import statistics
import pandas


def main():
    df = pandas.read_excel("./resources/employment_data.xlsx")
    print(df)
    new_df = pandas.DataFrame(
        columns=["employment_expectations_indicator",
                 "2015_first_quarter", "2015_second_quarter", "2015_third_quarter", "2015_fourth_quarter",
                 "2016_first_quarter", "2016_second_quarter", "2016_third_quarter", "2016_fourth_quarter",
                 "2017_first_quarter", "2017_second_quarter", "2017_third_quarter", "2017_fourth_quarter",
                 "2018_first_quarter", "2018_second_quarter", "2018_third_quarter", "2018_fourth_quarter",
                 "2019_first_quarter", "2019_second_quarter", "2019_third_quarter", "2019_fourth_quarter",
                 "2020_first_quarter", "2020_second_quarter", "2020_third_quarter", "2020_fourth_quarter",
                 "2021_first_quarter", "2021_second_quarter", "2021_third_quarter", "2021_fourth_quarter",
                 "2022_first_quarter", "2022_second_quarter", "2022_third_quarter", "2022_fourth_quarter",
                 "2023_first_quarter"
                 ])

    print(new_df)


if __name__ == '__main__':
    main()
