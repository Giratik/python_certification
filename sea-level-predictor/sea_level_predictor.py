import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Real Data')
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = reg.intercept+(reg.slope*x1)
    plt.plot(x1, y1, 'r', label='Prediction data from year 1880-2050')
    df_Y2000 = df.loc[df['Year']>=2000]
    reg_Y2000 = linregress(df_Y2000['Year'], df_Y2000['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = reg_Y2000.intercept+(reg_Y2000.slope*x2)
    plt.plot(x2, y2, 'g', label='Prediction data from year 2000-2050')
    plt.legend()
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    ax.set_xlim(1850, 2075)
    ax.set_ylim(df['CSIRO Adjusted Sea Level'].min() - 2, 20)
    plt.savefig('sea_level_plot.png')
    return plt.gca()