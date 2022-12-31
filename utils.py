import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


def load() -> pd.DataFrame:
    df = pd.read_pickle("new_data.pickle")

    outsample = df[df["Date Announced"] > "2019-01-01"] # true out of sample, do not touch
    insample = df[df["Date Announced"] <= "2019-01-01"]

    return outsample, insample 

def load_backtest_data() -> pd.DataFrame:
    df = pd.read_pickle("backtest_data.pickle")
    return df

def add_labels_inside_chart(x,y) -> None:
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

def add_labels_centered(x,y) -> None:
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
        
def chi_squared_test(table: np.array) -> str:
    #print("Checking independence by Chi Squared Test: ")
    stat, p, dof, expected = chi2_contingency(table)
    alpha = 0.05
    if p <= alpha:
        return "Dependent (reject H0)"
    else:
        return "Independent (fail to reject H0)"