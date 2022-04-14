import matplotlib.pyplot as plt
import seaborn as sns
from tshirt_data_female import new_data_f
from tshirt_data_male import new_data_m


def plot_data(df):
    sns.set()
    sns.scatterplot(y=df['stature'], x=df['weightkg'], c=df['color'])
    return plt.show()


def main():
    plot_data(new_data_m)
    plot_data(new_data_f)


if __name__ == '__main__':
    main()
