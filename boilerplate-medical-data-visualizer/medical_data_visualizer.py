import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# 2
df['overweight'] = None

# 3
df['overweight'] = np.where(df["weight"] /((df["height"]) / 100)**2> 25, 1, 0)

df['cholesterol'] = np.where(df['cholesterol']==1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
# 4
def draw_cat_plot():
  df_cat = None
  df_aacgosc = df[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']]
  df_cat = pd.melt(df_aacgosc, id_vars=['cardio'], var_name='variable', value_name='value')
  cat_plot = sns.catplot(df_cat, x='variable', hue='value', col='cardio', kind='count').set_axis_labels('variable', 'total').fig
  fig = None
  fig = cat_plot
  fig.savefig('catplot.png')
  return fig
# 10
def draw_heat_map():
  df_heat = df[(df['ap_lo']<=df['ap_hi'])&
             (df['height']>=df['height'].quantile(0.025))&
             (df['height']<=df['height'].quantile(0.975))&
             (df['weight']>=df['weight'].quantile(0.025))&
             (df['weight']<=df['weight'].quantile(0.975))]
  corr = df_heat.corr()
  mask = np.triu(np.ones_like(corr, dtype=bool))
  fig, ax = None, None
  fig, ax = plt.subplots(1, figsize=(10,10))
  sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')
  fig.savefig('heatmap.png')
  return fig