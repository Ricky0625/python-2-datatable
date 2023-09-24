import matplotlib.pyplot as plt
from load_csv import load


def convert_abbv_to_num(abbv: str) -> int:

    """
    converts numeric abbreviation to integer.
    for example, 4.2K to 4200
    """

    NUMS_ABBV = {
        "K": 1e3,
        "M": 1e6,
        "B": 1e9,
        "T": 1e12
    }

    abbv_key = abbv[-1]
    if abbv_key.isdigit():
        return int(abbv)

    abbv_value = NUMS_ABBV.get(abbv_key.upper())
    if abbv_value is None:
        raise ValueError(f"unable to recognize this abbreviation: {abbv[-1]}")
    return int(float(abbv.replace(abbv_key, '')) * abbv_value)


def main():

    """
    main
    """

    try:
        df = load("population_total.csv")

        # converts all the num abbreviation to a float number
        df.iloc[:, 1:] = df.iloc[:, 1:].map(convert_abbv_to_num)

        # filter data that ranges from 1800 to 2050
        filtered_df = df.loc[:, '1800':'2050']

        # extract all the years
        years = filtered_df.columns.astype(int)

        # Malaysia data
        malaysia = filtered_df.loc[df['country'] == "Malaysia"]
        malaysia_pop_data = malaysia.values.flatten()

        # other country's data
        other_country = 'France'
        other = filtered_df[df['country'] == other_country]
        other_pop_data = other.values.flatten()

        # plot data
        plt.plot(years, malaysia_pop_data, label='Malaysia', color='teal')
        plt.plot(years, other_pop_data, label=other_country, color='deeppink')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(range(min(years), max(years) + 1, 40))
        plt.title("Population Projections")
        plt.legend()
        plt.savefig("population_projection.png")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
