from load_csv import load


def main():
    df = load("../files/life_expectancy_years.csv")
    print(df)


if __name__ == "__main__":
    main()
