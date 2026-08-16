import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DensityPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the density plot.

        Calculated metrics:

        - Mean
        - Median
        - Skewness
        - Kurtosis
        """

        numbers = self.column.dropna()

        return {
            "Mean": numbers.mean(),
            "Median": numbers.median(),
            "Skewness": numbers.skew(),
            "Kurtosis": numbers.kurt()
        }

    def draw(self):
        column = self.column
        stats = self._stats()

        # ==========================
        # Figure
        # ==========================
        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Density / KDE
        # ==========================
        sns.kdeplot(
            x=column,
            fill=True,
            color="blue",
            alpha=0.3,
            linewidth=2,
            ax=ax
        )

        _, ymax = ax.get_ylim()

        # ==========================
        # Mean
        # ==========================
        ax.axvline(
            stats["Mean"],
            color="purple",
            linestyle="-.",
            label=f"Mean = {stats['Mean']:.2f}"
        )

        ax.text(
            stats["Mean"],
            ymax * 0.80,
            f"Mean\n{stats['Mean']:.2f}",
            color="purple",
            fontsize=8,
            ha="center",
            va="top",
            rotation=90,
            backgroundcolor="white"
        )

        # ==========================
        # Median
        # ==========================
        ax.axvline(
            stats["Median"],
            color="red",
            label=f"Median = {stats['Median']:.2f}"
        )

        ax.text(
            stats["Median"],
            ymax * 0.95,
            f"Median\n{stats['Median']:.2f}",
            color="red",
            fontsize=8,
            ha="center",
            va="top",
            rotation=90,
            backgroundcolor="white"
        )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"Density Plot - {column.name}"
        )

        ax.set_xlabel(
            column.name
        )

        ax.set_ylabel(
            "Density"
        )

        # ==========================
        # Grid & Legend
        # ==========================
        ax.grid(True)

        ax.legend()

        # ==========================
        # Layout
        # ==========================
        plt.tight_layout()

        plt.show()
