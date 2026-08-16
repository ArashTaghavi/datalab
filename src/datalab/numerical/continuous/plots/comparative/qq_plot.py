import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import math


class QQPlot:

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Calculate Grid
        # ---------------------------------

        n = len(self.columns)

        ncols = math.ceil(math.sqrt(n))
        nrows = math.ceil(n / ncols)

        # ---------------------------------
        # Plot
        # ---------------------------------

        fig, axes = plt.subplots(nrows, ncols, figsize=(6 * ncols, 5 * nrows), dpi=200)

        axes = [axes] if n == 1 else axes.flatten()

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
        # Hide Empty Axes
        # ---------------------------------

        for ax in axes[n:]:
            ax.set_visible(False)

        # ---------------------------------
        # Main Title
        # ---------------------------------

        fig.suptitle("Normality Comparison - QQ Plot", fontsize=12)

        plt.tight_layout()

        plt.show()
