import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')
df.index = pd.to_datetime(df.index)
df = df[(df['value'] >= (df['value'].quantile(0.025))) & (df['value'] <= (df['value'].quantile(0.975)))]

def draw_line_plot():
  fig, ax = plt.subplots(figsize=(15, 5))
  plt.plot(df.index, df['value'], 'r')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set(xlabel='Date', ylabel='Page Views')
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  df_bar = df.copy()
  df_bar['year'] = [d.year for d in df.index]
  df_bar['month'] = [d.month for d in df.index]
  df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=df_bar, x='year', y='value', hue='month', ax=ax, palette="Paired")
  handles, labels = ax.get_legend_handles_labels()
  ax.legend(handles=handles[1:], labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months', loc='upper left')
  ax.set(xlabel='Years', ylabel='Average Page Views')
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df.index]
  df_box['month'] = [d.strftime('%b') for d in df.index]
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  df_box.sort_values('month', key = lambda x : pd.Categorical(x, categories=months, ordered=True), inplace=True)
  fig, ax = plt.subplots(1, 2, figsize=(20, 10))
  sns.boxplot(df_box, x='year', y='value', ax=ax[0], palette="Set1")
  sns.boxplot(df_box, x='month', y='value', ax=ax[1], palette="gist_rainbow")
  ax[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
  ax[1].set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')
  fig.savefig('box_plot.png')
  return fig