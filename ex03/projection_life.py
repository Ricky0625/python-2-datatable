from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def main():

    """
    main
    """

    try:
        # load datasets
        life_expectancy_df = load("life_expectancy_years.csv")
        income_inflation_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )

        # check if one of the dataframe is None
        if life_expectancy_df is None or income_inflation_df is None:
            raise AssertionError("failed to load csv")

        # filter out the data from both dataframe
        target_year = '1900'
        filtered_le_df = life_expectancy_df.loc[:, target_year]
        filtered_ii_df = income_inflation_df.loc[:, target_year]

        # plot a scatter plot
        plt.scatter(filtered_ii_df, filtered_le_df)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')

        # change scale for x-axis to using log
        plt.xscale('log')

        # format the x-axis labels using EngFormatter
        plt.gca().xaxis.set_major_formatter(EngFormatter(sep=""))

        # set plot title
        plt.title(target_year)

        # show plot
        plt.show()
    except KeyboardInterrupt:
        plt.close()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
