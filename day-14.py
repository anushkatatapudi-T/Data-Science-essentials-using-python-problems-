import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('couples.csv')
# print(df)
df=df.set_index('decade')
# df.plot()
# plt.show()
focus_column='online'
focus_color='C3'
back_columns=[
    'college','at work','through friends',
    'through family','restaurant','neighbors'
]
back_colors=['C0','C1','C2','C4','C5','C6']
df.plot(y=back_columns, color=back_colors, alpha=0.5)
plt.plot(df.index, df[focus_column], color=focus_color, linewidth=5)
plt.show()
def add_axes_labels( ):
    y_ticks = [0, 10, 20, 30, 40, 50]
    y_tick_labels = ['0', '10', '20', '30', '40', '50%']
    plt.yticks(y_ticks, y_tick_labels)
    plt.xlabel('Decade')
#python function
# def clean_axes( ):
#     ax=plt.gca()
#     ax.spines[['left','top','right']].set_visible(False)
#     ax.tick_params(axis='y',length=0)
#     plt.grid(axis='y',alpha=0.5)