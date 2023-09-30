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
        df = load("../files/life_expectancy_years.csv")

        # .loc is used to select and access a group of rows and columns
        # df.loc[row_labels, column_labels]
        # df['country'] == name creates a Boolean Series where each element
        # is True if the corresponding 'country' column value is equal to
        # the "name"
        country_data = df.loc[df['country'] == name]

        # extract the years from the column names
        # skip the country name columns
        years = country_data.columns[1:].astype(int)

        # : - "select all rows"
        # 1: - "select all cols starting from index 1"
        # flatten: transform multi-dimensional array to 1D array
        life_expectancy = country_data.values[:, 1:].flatten()

        # plot graph. plot(x-axis, y-axis)
        plt.plot(years, life_expectancy)

        # adjust x-axis ticks
        plt.xticks(range(min(years), max(years) + 1, 40))

        # set labels and title
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(f"{name} Life expectancy Projections")
        plt.show()
    except AssertionError as e:
        print(f"[ERROR]: {e}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
