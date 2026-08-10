import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

from ....contracts.plot import Plot

class QQPlot(Plot):

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=200)

        axes = axes.flatten()

        # ---------------------------------
        # QQ Plots
        # ---------------------------------
        for ax, column, title in zip(axes, self.columns, self.titles):
            values = column.dropna()

            stats.probplot(values, dist="norm", plot=ax)

            ax.set_title(title, fontsize=10)

            ax.set_xlabel("Theoretical Quantiles", fontsize=9)

            ax.set_ylabel("Sample Quantiles", fontsize=9)

            ax.grid(True, alpha=0.3)

        # ---------------------------------
        # Main Title
        # ---------------------------------
        fig.suptitle("Normality Comparison - QQ Plot", fontsize=12)

        plt.tight_layout()

        plt.show()
