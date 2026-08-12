import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from ....contracts.plot import Plot


class HistogramPlot(Plot):

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Prepare data
        # ---------------------------------
        data = []

        for column, title in zip(self.columns, self.titles):

            values = column.dropna()

            for value in values:
                data.append({"Value": value, "Distribution": title})

        data = pd.DataFrame(data)

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        sns.histplot(
            data=data,
            x="Value",
            hue="Distribution",
            multiple="dodge",
            discrete=True,
            shrink=0.8,
            ax=ax,
        )

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Distribution Comparison - Histogram", fontsize=12)

        ax.set_xlabel("Value", fontsize=10)

        ax.set_ylabel("Frequency", fontsize=10)

        # ---------------------------------
        # Grid
        # ---------------------------------
        ax.grid(True, axis="y", alpha=0.3)

        plt.xticks(fontsize=9)

        plt.yticks(fontsize=9)

        plt.tight_layout()

        plt.show()
