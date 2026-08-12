import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class CDFPlot:

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        colors = sns.color_palette("tab10", len(self.columns))

        for column, title, color in zip(self.columns, self.titles, colors):
            values = column.dropna().sort_values()

            cdf = values.rank(method="first") / len(values)

            ax.plot(values, cdf, linewidth=2, color=color, label=title)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Distribution Comparison - CDF", fontsize=12)

        ax.set_xlabel("Value", fontsize=10)

        ax.set_ylabel("Cumulative Probability", fontsize=10)

        # ---------------------------------
        # Y-axis
        # ---------------------------------
        ax.set_ylim(0, 1)

        # ---------------------------------
        # Grid & Legend
        # ---------------------------------
        ax.grid(True, alpha=0.3)

        ax.legend(fontsize=9)

        plt.tight_layout()

        plt.show()
