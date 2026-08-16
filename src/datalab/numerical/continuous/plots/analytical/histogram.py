import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class HistogramPlot:

    def __init__(self, column: pd.Series):
        self.column = column

    def _stats(self):
        """
        Calculate statistics required for the histogram plot.

        Calculated metrics:

        - Median
        - Mean
        - Lower Outlier Bound
        - Upper Outlier Bound
        - Outlier Values
        """

        numbers = self.column

        # -----------------------------
        # Quartiles
        # -----------------------------
        q1 = numbers.quantile(0.25)
        q3 = numbers.quantile(0.75)

        # -----------------------------
        # Interquartile Range
        # -----------------------------
        iqr = q3 - q1

        # -----------------------------
        # Outlier Detection Bounds
        # -----------------------------
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        # -----------------------------
        # Outliers
        # -----------------------------
        outliers = numbers[
            (numbers < lower) |
            (numbers > upper)
            ]

        return {
            "Median": numbers.median(),
            "Mean": numbers.mean(),
            "Lower": lower,
            "Upper": upper,
            "Outliers": outliers
        }

    def draw(self, bins=15):

        column = self.column
        stats = self._stats()

        fig, ax = plt.subplots(
            figsize=(15, 5),
            dpi=200
        )

        # ==========================
        # Histogram + KDE
        # ==========================
        sns.histplot(
            x=column,
            bins=bins,
            kde=True,
            edgecolor="black",
            ax=ax
        )

        _, ymax = ax.get_ylim()

        # ==========================
        # Lower Bound
        # ==========================
        ax.axvline(
            stats["Lower"],
            color="blue",
            linestyle="--",
            label=f"Lower = {stats['Lower']:.2f}"
        )

        ax.text(
            stats["Lower"],
            ymax * 0.95,
            f"Lower\n{stats['Lower']:.2f}",
            color="blue",
            fontsize=8,
            ha="center",
            va="top",
            rotation=90,
            backgroundcolor="white"
        )

        # ==========================
        # Upper Bound
        # ==========================
        ax.axvline(
            stats["Upper"],
            color="blue",
            linestyle="--",
            label=f"Upper = {stats['Upper']:.2f}"
        )

        ax.text(
            stats["Upper"],
            ymax * 0.95,
            f"Upper\n{stats['Upper']:.2f}",
            color="blue",
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
            ymax * 0.75,
            f"Mean\n{stats['Mean']:.2f}",
            color="purple",
            fontsize=8,
            ha="center",
            va="top",
            rotation=90,
            backgroundcolor="white"
        )

        # ==========================
        # Outliers
        # ==========================
        if not stats["Outliers"].empty:

            for value in stats["Outliers"]:
                ax.axvline(
                    value,
                    color="red",
                    linestyle=":"
                )

                ax.text(
                    value,
                    ymax * 0.55,
                    f"Outlier\n{value:.2f}",
                    color="red",
                    fontsize=7,
                    ha="center",
                    va="top",
                    rotation=90,
                    backgroundcolor="white"
                )

            ax.plot(
                [],
                [],
                color="red",
                linestyle=":",
                label=f"Outliers = {list(stats['Outliers'])}"
            )

        # ==========================
        # Labels
        # ==========================
        ax.set_title(
            f"Histogram + KDE - {column.name}"
        )

        ax.set_xlabel(column.name)

        ax.set_ylabel("Frequency")

        # ==========================
        # Grid & Legend
        # ==========================
        ax.grid(True)

        ax.legend()

        plt.show()
