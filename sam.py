import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("C:/Users/Arshpreet/Desktop/medical_examination.csv")

df['overweight'] = (df['weight']/(df['height']/100)**2>25).astype(int)
df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)
#print(df)
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0: 'total'})

    graph=sns.catplot(data=df_cat, x="variable", y="total", hue="value",col="cardio")

    # 8
    fig = graph.fig()
    fig.savefig('catplot.png')
    return fig