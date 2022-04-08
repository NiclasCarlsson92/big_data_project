import matplotlib.pyplot as plt
import seaborn as sns
from get_data_female import new_data_f
from get_data_male import new_data_m


def plot_female():
    sns.set()
    sns.scatterplot(y=new_data_f['stature'], x=new_data_f['weightkg'], c=new_data_f['color'])
    return plt.show()


def plot_male():
    sns.set()
    sns.scatterplot(y=new_data_m['stature'], x=new_data_m['weightkg'], c=new_data_m['color'])
    return plt.show()


def main():
    #plot_female()
    plot_male()


if __name__ == '__main__':
    main()
