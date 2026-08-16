import matplotlib.pyplot as plt
import pandas as pd

class MeanStdPlot:

    def __init__(self, columns: list[pd.Series], titles: list[str]):
        self.columns = columns
        self.titles = titles

    def draw(self):

        if len(self.columns) != len(self.titles):
            raise ValueError("The number of columns must match the number of titles.")

        # ---------------------------------
        # Calculate statistics
        # ---------------------------------

        means = [column.dropna().mean() for column in self.columns]

        stds = [column.dropna().std() for column in self.columns]

        # ---------------------------------
        # Plot
        # ---------------------------------

        fig, ax = plt.subplots(figsize=(14, 7), dpi=200)

        x = list(range(len(self.columns)))

        ax.errorbar(x, means, yerr=stds, fmt="o", markersize=7, capsize=8, linewidth=2)

        # ---------------------------------
        # Annotations
        # ---------------------------------

        for i, (mean, std) in enumerate(zip(means, stds)):

            lower = mean - std
            upper = mean + std

            # ---------------------------------
            # Mean + SD
            # ---------------------------------

            ax.annotate(
                f"Mean + SD = {upper:.2f}",
                xy=(i, upper),
                xytext=(10, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
            )

            # ---------------------------------
            # SD
            # ---------------------------------

            ax.annotate(
                f"SD = {std:.2f}",
                xy=(i, mean),
                xytext=(-10, 0),
                textcoords="offset points",
                ha="right",
                va="center",
                fontsize=8,
            )

            # ---------------------------------
            # Mean
            # ---------------------------------

            ax.annotate(
                f"Mean = {mean:.2f}",
                xy=(i, mean),
                xytext=(10, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
            )

            # ---------------------------------
            # Mean - SD
            # ---------------------------------

            ax.annotate(
                f"Mean - SD = {lower:.2f}",
                xy=(i, lower),
                xytext=(10, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                fontsize=8,
            )

        # ---------------------------------
        # Labels
        # ---------------------------------

        ax.set_title("Mean ± Standard Deviation Comparison", fontsize=12)

        ax.set_xlabel("Distribution", fontsize=10)

        ax.set_ylabel("Value", fontsize=10)

        ax.set_xticks(x)

        ax.set_xticklabels(self.titles, fontsize=9)

        # ---------------------------------
        # Grid
        # ---------------------------------

        ax.grid(True, axis="y", alpha=0.3)

        ax.margins(x=0.15)

        plt.tight_layout()

        plt.show()
