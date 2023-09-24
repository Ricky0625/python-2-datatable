from load_csv import load
import matplotlib.pyplot as plt


def main():

    """
    main
    """

    try:
        name = "Malaysia"

        # return a data frame
        # a data frame typically have both column and row names
        df = load("life_expectancy_years.csv")

        # return a data frame containing all the rows where 'country'
        # matches the value specified by the 'name'
        country_data = df.loc[df['country'] == name]

        # extract the years from the column names
        years = country_data.columns[1:].astype(int)

        # : - "select all rows"
        # 1: - "select all cols starting from index 1"
        life_expectancy = country_data.values[:, 1:].flatten()

        plt.plot(years, life_expectancy)
        plt.xticks(range(min(years), max(years) + 1, 40))
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(f"{name} Life expectancy Projections")
        # plt.show()
        plt.savefig(f"{name}.png")
    except AssertionError as e:
        print(f"[ERROR]: {e}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
