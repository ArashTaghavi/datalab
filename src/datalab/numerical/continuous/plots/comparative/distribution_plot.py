import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DistributionPlot:

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Prepare data
        # ---------------------------------
        values = [column.dropna().to_numpy() for column in self.columns]

        # ---------------------------------
        # Plot
        # ---------------------------------
        fig, ax = plt.subplots(figsize=(12, 6), dpi=200)

        colors = sns.color_palette("tab10", len(values))

        for column, title, color in zip(values, self.titles, colors):

            # KDE
            sns.kdeplot(column, color=color, linewidth=2, ax=ax, label=title)

        # ---------------------------------
        # Labels
        # ---------------------------------
        ax.set_title("Distribution Comparison", fontsize=12)

        ax.set_xlabel("Value", fontsize=10)

        ax.set_ylabel("Density", fontsize=10)

        # ---------------------------------
        # Grid & Legend
        # ---------------------------------
        ax.grid(True, alpha=0.3)

        ax.legend(fontsize=9)

        plt.tight_layout()

        plt.show()
